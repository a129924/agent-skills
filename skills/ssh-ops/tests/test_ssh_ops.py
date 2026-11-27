"""Regression tests for the runner and a disposable, local directory source."""

import hashlib
import io
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import ssh_askpass as askpass  # noqa: E402
import ssh_ops as ops  # noqa: E402


class LocalMaster:
    """Run fixed remote reads in a POSIX shell against disposable fixtures."""

    deadline = 0

    def command(self, command):
        return ["/bin/sh", "-c", command]

    def require_same(self, identity):
        if identity != (1, 2, 3):
            raise AssertionError("unexpected master")


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.source = self.root / "source"
        self.source.mkdir()
        self.parent = self.root / "destination"
        self.parent.mkdir(mode=0o700)
        self.master = LocalMaster()
        self.master.deadline = time.monotonic() + 20
        self.identity = (1, 2, 3)

    def command(self, program, deadline=5):
        return ops.capture_command([sys.executable, "-c", program], time.monotonic() + deadline)

    def test_resolves_trusted_alias_and_fails_mismatched_endpoint(self):
        config = self.root / "config"
        config.write_text("Host alias\n HostName localhost\n Port 2201\n User reports\n")
        args = SimpleNamespace(target="alias", config=config, expect=["reports", "localhost", "2201"])
        target = ops.Target(args, time.monotonic() + 5)
        self.assertEqual(target.endpoint, {"host": "localhost", "port": 2201, "user": "reports"})
        command = ops.Master(target, self.root / "absent.sock", time.monotonic() + 5).command("id")
        self.assertIn("ProxyCommand=/usr/bin/false", command)
        self.assertEqual(command[-3:], ["--", "alias", "id"])
        args.expect[-1] = "22"
        with self.assertRaisesRegex(ops.Stop, "differs"):
            ops.Target(args, time.monotonic() + 5)

    def test_inspects_includes_before_resolving_executable_match(self):
        config = self.root / "config"
        child = self.root / "included.conf"
        config.write_text(f'Include "{child}"\n')
        child.write_text('Match !exec "echo unexpected"\n')
        with patch.object(ops, "ssh_effective") as resolve:
            with self.assertRaisesRegex(ops.Stop, "Match exec"):
                ops.Target(SimpleNamespace(target="alias", config=config), time.monotonic() + 5)
        resolve.assert_not_called()

    def test_ambiguous_include_syntax_is_rejected_without_opening_ssh(self):
        config = self.root / "config"
        for value in ('"/tmp/include#unexpected"', r"/tmp/include\path"):
            config.write_text(f"Include {value}\n")
            with self.subTest(value=value), self.assertRaisesRegex(ops.Stop, "SSH Include"):
                ops.inspect_configs(config)

    def test_watchdog_reaps_child_and_lease_on_supervisor_disconnect(self):
        lease = self.root / "watch"
        lease.mkdir(mode=0o700)
        (lease / "prompt").touch()
        argv = [sys.executable, "-c", """
import sys
import time
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import ssh_ops
sys.exit(ssh_ops.watch_master(Path(sys.argv[2]), time.monotonic() + 10,
                             [sys.executable, "-c", "import time; time.sleep(30)"]))
""", str(SCRIPTS), str(lease)]
        with subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              start_new_session=True) as watcher:
            pid = int(watcher.stdout.readline())
            watcher.stdin.close()
            self.assertEqual(watcher.wait(timeout=5), 0)
            with self.assertRaises(ProcessLookupError):
                os.kill(pid, 0)
        self.assertFalse(lease.exists())

    def test_command_drains_both_streams_and_reports_nonzero(self):
        result = self.command("import os,sys; os.write(1,b'a'*70000); os.write(2,b'b'*71000); sys.exit(7)")
        self.assertEqual(result["ssh_exit_code"], 7)
        self.assertEqual(result["status"], "remote-nonzero")
        self.assertEqual(result["stdout"], "a" * 65536)
        self.assertEqual(result["stderr"], "b" * 65536)
        self.assertEqual(result["truncated"], {"stdout": True, "stderr": True})

    def test_unknown_command_and_timeout(self):
        result = self.command("import sys; sys.exit(255)")
        self.assertEqual((result["status"], result["ssh_exit_code"]), ("unknown", 255))
        result = self.command("import time; time.sleep(5)", deadline=0.1)
        self.assertEqual((result["status"], result["ssh_exit_code"]), ("unknown", None))

    def test_missing_master_stops_before_command(self):
        args = SimpleNamespace(target="localhost", config=None, seconds=5, lease=None,
                               socket=self.root / "absent", operation="exec")
        with patch.object(ops, "capture_command") as dispatch:
            with self.assertRaisesRegex(ops.Stop, "socket is unavailable"):
                ops.run_operation(args)
        dispatch.assert_not_called()

    def test_lease_serializes_actions(self):
        lease = self.root / "lease"
        lease.mkdir(mode=0o700)
        ops.write_private(lease / "lease.json", '{"test": 1}')
        with ops.task_binding(lease):
            with self.assertRaisesRegex(ops.Stop, "another operation"):
                with ops.task_binding(lease):
                    self.fail("a second lease was acquired")

    @unittest.skipUnless(shutil.which("sha256sum"), "sha256sum is needed for the local remote fixture")
    def test_single_file_preserves_exact_bytes_mode_and_collision(self):
        source = self.source / "quote's file"
        payload = b"hello\0world\n"
        source.write_bytes(payload)
        result = ops.download_file(self.master, self.identity, str(source), self.parent, "out")
        path = self.parent / "out"
        self.assertEqual(path.read_bytes(), payload)
        self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)
        self.assertEqual(result["sha256"], hashlib.sha256(payload).hexdigest())
        source.write_bytes(b"new")
        with self.assertRaisesRegex(ops.Stop, "exclusive file install"):
            ops.download_file(self.master, self.identity, str(source), self.parent, "out")
        self.assertEqual(list(self.parent.iterdir()), [path])
        self.assertEqual(path.read_bytes(), payload)

    @unittest.skipUnless(sys.platform == "darwin", "macOS exclusive rename")
    def test_nested_directory_empty_folder_binary_and_atomic_collision(self):
        (self.source / "nested" / "empty").mkdir(parents=True)
        (self.source / "nested" / "body").write_bytes(b"file\0payload\n")
        result = ops.download_directory(self.master, self.identity, str(self.source), self.parent, "out")
        path = self.parent / "out"
        self.assertEqual((result["files"], result["bytes"]), (1, 13))
        self.assertTrue((path / "nested" / "empty").is_dir())
        self.assertEqual((path / "nested" / "body").read_bytes(), b"file\0payload\n")
        self.assertEqual(stat.S_IMODE((path / "nested").stat().st_mode), 0o700)
        self.assertEqual(stat.S_IMODE((path / "nested" / "body").stat().st_mode), 0o600)
        with self.assertRaisesRegex(ops.Stop, "exclusive directory install"):
            ops.download_directory(self.master, self.identity, str(self.source), self.parent, "out")
        self.assertEqual(list(self.parent.iterdir()), [path])

    def test_remote_links_and_special_entries_are_rejected(self):
        path = self.source / "link"
        path.symlink_to(self.root, target_is_directory=True)
        for remote in (self.source, path):
            with self.assertRaises(ops.Stop):
                ops.download_directory(self.master, self.identity, str(remote), self.parent, "out")
        path.unlink()
        os.mkfifo(self.source / "pipe")
        with self.assertRaises(ops.Stop):
            ops.download_directory(self.master, self.identity, str(self.source), self.parent, "out")
        self.assertEqual(list(self.parent.iterdir()), [])

    def test_framing_rejects_escape_duplicate_fields_and_truncation(self):
        for header in (
            b'{"type":"dir","path":[".."]}\n',
            b'{"type":"dir","path":["/escaped"]}\n',
            b'{"type":"dir","path":[],"path":[]}\n',
            b'{"type":"dir","path":[]}',
            b"x" * (ops.HEADER_LIMIT + 1),
        ):
            with self.subTest(header=header[:100]), self.assertRaises(ops.Stop):
                ops.frame(header, False)

    def test_short_and_wrong_file_contents_fail_verification(self):
        digest = hashlib.sha256(b"correct").hexdigest()
        expected = {(): (), ("file",): (7, digest)}
        prefix = b'{"type":"dir","path":[]}\n{"type":"file","path":["file"],"size":7}\n'
        for index, payload in enumerate((b"short", b"damaged")):
            path = self.parent / str(index)
            path.mkdir()
            fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
            try:
                with self.assertRaises(ops.Stop):
                    ops.directory_entries(io.BytesIO(prefix + payload), expected=expected, local=fd)
            finally:
                os.close(fd)

    def test_candidate_key_is_pinned_only_after_fingerprint_match(self):
        key = self.root / "key"
        subprocess.run([ops.KEYGEN, "-q", "-t", "ed25519", "-N", "", "-f", str(key)], check=True)
        public = key.with_suffix(".pub")
        fingerprint = subprocess.check_output([ops.KEYGEN, "-E", "sha256", "-lf", public]).split()[1].decode()
        directory = self.root / "lease"
        directory.mkdir(mode=0o700)
        target = SimpleNamespace(endpoint={"host": "example.test", "port": 2222}, effective={})
        args = SimpleNamespace(pin_key=public, fingerprint="SHA256:wrong")
        with self.assertRaisesRegex(ops.Stop, "does not match"):
            ops.known_host_pin(target, args, directory, time.monotonic() + 5)
        self.assertEqual(list(directory.iterdir()), [])
        args.fingerprint = fingerprint
        options = ops.known_host_pin(target, args, directory, time.monotonic() + 5)
        self.assertIn(str(directory / "known_hosts"), options["UserKnownHostsFile"])
        self.assertTrue((directory / "known_hosts").read_text().startswith("[example.test]:2222 ssh-ed25519 "))

    def test_mock_askpass_keeps_answer_in_pipe_and_lifecycle_in_status(self):
        status = self.root / "prompt"
        status.touch()
        secret = b"disposable-test-answer"
        pipe = SimpleNamespace(buffer=io.BytesIO())
        env = {"SSH_OPS_PROMPT_STATUS": str(status), "SSH_OPS_PROMPT_TARGET": "reports@example.test:22",
               "SSH_OPS_PROMPT_SECONDS": "10"}
        with patch.dict(os.environ, env), patch.object(askpass.sys, "stdout", pipe):
            with patch.object(askpass.subprocess, "run", return_value=SimpleNamespace(
                returncode=0, stderr=b"", stdout=secret + b"\n"
            )) as dialog:
                self.assertEqual(askpass.main(), 0)
        self.assertEqual(pipe.buffer.getvalue(), secret + b"\n")
        self.assertEqual(status.read_text(), "submitted\n")
        self.assertNotIn(secret.decode(), repr(dialog.call_args))

    def test_password_prompt_is_consumed_after_first_claim(self):
        status = self.root / "prompt"
        status.touch()
        self.assertTrue(askpass.claim_prompt(status))
        askpass.set_status(status, "submitted")
        self.assertFalse(askpass.claim_prompt(status))

    def test_cancel_waits_for_supervisor_and_emits_no_answer(self):
        status = self.root / "prompt"
        status.touch()
        pipe = SimpleNamespace(buffer=io.BytesIO())
        env = {"SSH_OPS_PROMPT_STATUS": str(status), "SSH_OPS_PROMPT_TARGET": "reports@example.test:22",
               "SSH_OPS_PROMPT_SECONDS": "10"}
        with patch.dict(os.environ, env), patch.object(askpass.sys, "stdout", pipe):
            with patch.object(askpass.subprocess, "run", return_value=SimpleNamespace(
                returncode=1, stderr=b"SSH dialog canceled (-128)", stdout=b""
            )), patch.object(askpass.time, "sleep") as wait:
                self.assertEqual(askpass.main(), 1)
        wait.assert_called_once()
        self.assertEqual(status.read_text(), "canceled\n")
        self.assertEqual(pipe.buffer.getvalue(), b"")


if __name__ == "__main__":
    unittest.main()
