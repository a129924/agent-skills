"""Bounded macOS SSH actions. Bootstrap and socket reuse have separate permissions."""

import argparse
from contextlib import contextmanager
import ctypes
import fcntl
import glob
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import re
import select
import selectors
import shlex
import shutil
import signal
import stat
import subprocess
import sys
import tempfile
import threading
import time

SSH = "/usr/bin/ssh"
KEYGEN = "/usr/bin/ssh-keygen"
FALSE = "/usr/bin/false"
OUTPUT_LIMIT = 65536
HEADER_LIMIT = 65536
CHUNK = 65536
DIGEST = re.compile(r"[0-9a-f]{64}")
USERNAME = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.-]*")
HOSTNAME = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.-]*")
SAFE_OPTIONS = {
    "CanonicalizeHostname": "no",
    "ClearAllForwardings": "yes",
    "ForwardAgent": "no",
    "ForwardX11": "no",
    "ForkAfterAuthentication": "no",
    "KnownHostsCommand": "none",
    "PermitLocalCommand": "no",
    "ProxyUseFdpass": "no",
    "RemoteCommand": "none",
    "Tunnel": "no",
}
EFFECTIVE_SAFETY = {
    "canonicalizehostname": "false",
    "clearallforwardings": "yes",
    "forwardagent": "no",
    "forwardx11": "no",
    "forkafterauthentication": "no",
    "permitlocalcommand": "no",
    "proxyusefdpass": "no",
    "requesttty": "false",
    "tunnel": "false",
}


class Stop(Exception):
    def __init__(self, phase, reason):
        super().__init__(reason)
        self.phase = phase


def emit(data):
    print(json.dumps(data, ensure_ascii=True), flush=True)


def seconds_left(deadline):
    seconds = deadline - time.monotonic()
    if seconds <= 0:
        raise TimeoutError
    return seconds


def options(values):
    return [flag for key, value in values.items() for flag in ("-o", f"{key}={value}")]


def checked_host(value):
    if HOSTNAME.fullmatch(value):
        return value
    try:
        return str(ipaddress.IPv6Address(value.removeprefix("[").removesuffix("]")))
    except ValueError:
        raise Stop("target", "invalid SSH host or alias") from None


def checked_target(target):
    user, at, host = target.rpartition("@")
    if at and not USERNAME.fullmatch(user):
        raise Stop("target", "invalid SSH account")
    return (f"{user}@" if at else "") + checked_host(host)


def inspect_configs(config):
    """Inspect trust inputs before ssh -G, which can otherwise execute Match exec."""
    home = Path.home() / ".ssh"
    roots = [(config, home, True)] if config else [
        (home / "config", home, False),
        (Path("/etc/ssh/ssh_config"), Path("/etc/ssh"), False),
    ]
    seen = set()
    while roots:
        path, include_base, required = roots.pop()
        try:
            path = path.resolve(strict=True)
        except FileNotFoundError:
            if required:
                raise Stop("config", "trusted configuration file is missing") from None
            continue
        key = (path, include_base)
        if key in seen:
            continue
        seen.add(key)
        info = path.stat()
        if not stat.S_ISREG(info.st_mode) or info.st_uid not in (0, os.getuid()) or info.st_mode & 0o022:
            raise Stop("config", "configuration source is not an owned, protected regular file")
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.lstrip()
            if not line or line.startswith("#"):
                continue
            match = re.match(r"([A-Za-z]+)(?:[\s=]+|$)(.*)", line)
            if not match:
                raise Stop("config", "unable to inspect SSH configuration syntax")
            keyword, value = match[1].lower(), match[2]
            if keyword == "match" and re.search(r"(?<![A-Za-z])exec(?![A-Za-z])", value, re.I):
                raise Stop("config", "Match exec requires an equivalent configuration without the hook")
            if keyword == "include":
                try:
                    if "\\" in value or "#" in value:
                        raise ValueError
                    entries = shlex.split(value)
                except ValueError:
                    raise Stop("config", "unable to inspect SSH Include") from None
                for entry in entries:
                    if any(c in entry for c in "%$\\") or (entry.startswith("~") and not entry.startswith("~/")):
                        raise Stop("config", "cannot verify an expanded SSH Include")
                    candidate = Path(entry).expanduser()
                    if not candidate.is_absolute():
                        candidate = include_base / candidate
                    for included in glob.glob(str(candidate)):
                        roots.append((Path(included), include_base, True))


def ssh_effective(argv, target, deadline):
    result = subprocess.run(
        [*argv, "-G", "--", target], stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
        timeout=min(10, seconds_left(deadline)), check=False,
    )
    if result.returncode:
        raise Stop("config", "OpenSSH could not resolve the effective configuration")
    return dict(line.split(" ", 1) for line in result.stdout.decode().splitlines() if " " in line)


def endpoint(effective):
    try:
        user = effective["user"]
        port = int(effective["port"])
        if not USERNAME.fullmatch(user) or not 1 <= port <= 65535:
            raise ValueError
        return {"host": checked_host(effective["hostname"]), "port": port, "user": user}
    except (KeyError, ValueError):
        raise Stop("target", "unable to verify effective SSH endpoint") from None


class Target:
    def __init__(self, args, deadline):
        self.selector = checked_target(args.target)
        if args.config and not args.config.is_absolute():
            raise Stop("config", "specify the absolute path to the trusted configuration")
        self.config = args.config.resolve(strict=True) if args.config else None
        inspect_configs(self.config)
        self.base = [SSH, *([] if self.config is None else ["-F", str(self.config)]), "-nT"]
        self.effective = ssh_effective(
            [*self.base, *options({"CanonicalizeHostname": "no"})], self.selector, deadline
        )
        self.endpoint = endpoint(self.effective)
        expected = getattr(args, "expect", None)
        if expected:
            expected_user, expected_host, expected_port = expected
            if not expected_port.isdecimal():
                raise Stop("target", "expected port must be numeric")
            if self.endpoint != {"host": checked_host(expected_host),
                                 "port": int(expected_port), "user": expected_user}:
                raise Stop("target", "effective endpoint differs from the approved endpoint")

    def verified_argv(self, socket_path, deadline, extra, effective):
        inspect_configs(self.config)
        argv = [
            *self.base, "-S", str(socket_path),
            "-l", self.endpoint["user"], "-p", str(self.endpoint["port"]),
            *options({"HostName": self.endpoint["host"], **SAFE_OPTIONS, **extra}),
        ]
        observed = ssh_effective(argv, self.selector, deadline)
        expected = {**EFFECTIVE_SAFETY, **effective}
        if endpoint(observed) != self.endpoint or any(
            observed.get(key, "none") != value for key, value in expected.items()
        ):
            raise Stop("config", "OpenSSH does not enforce the required settings")
        return argv


def private_directory(path):
    if not path.is_absolute() or path != path.resolve():
        raise Stop("path", "use the absolute, resolved private directory")
    info = path.stat()
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077:
        raise Stop("path", "directory must be private and owned by the current user")
    return path


def socket_id(path):
    if not path.is_absolute() or str(path) != os.path.realpath(path) or any(c in str(path) for c in "%$\n\r"):
        raise Stop("master", "use the exact resolved controller socket path")
    info = path.lstat()
    if not stat.S_ISSOCK(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077:
        raise Stop("master", "controller must be an owned, private Unix socket")
    return info.st_dev, info.st_ino


class Master:
    def __init__(self, target, path, deadline):
        self.path = path
        self.target = target
        self.deadline = deadline
        self.bound_identity = None
        self.argv = target.verified_argv(
            path, deadline,
            {"ControlMaster": "no", "ControlPersist": "no", "BatchMode": "yes",
             "ProxyCommand": FALSE, "SessionType": "default"},
            {"controlmaster": "false", "controlpersist": "no", "batchmode": "yes",
             "proxycommand": FALSE, "sessiontype": "default"},
        )

    def identity(self):
        try:
            before = socket_id(self.path)
            check = subprocess.run(
                [*self.argv, "-O", "check", "--", self.target.selector],
                stdin=subprocess.DEVNULL, capture_output=True,
                timeout=min(5, seconds_left(self.deadline)), check=False,
            )
            match = re.search(rb"Master running \(pid=([1-9][0-9]*)\)", check.stderr + check.stdout)
            if check.returncode != 0 or not match or before != socket_id(self.path):
                raise Stop("master", "controller is unavailable or changed")
        except FileNotFoundError:
            raise Stop("master", "controller socket is unavailable") from None
        return (*before, int(match[1]))

    def require_same(self, identity):
        if self.identity() != identity:
            raise Stop("master", "controller changed during this operation")

    def command(self, command):
        if self.bound_identity is not None:
            self.require_same(self.bound_identity)
        return [*self.argv, "--", self.target.selector, command]

    def close(self, identity):
        try:
            self.require_same(identity)
        except (Stop, TimeoutError, subprocess.TimeoutExpired):
            return False
        result = subprocess.run(
            [*self.argv, "-O", "exit", "--", self.target.selector],
            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            timeout=min(5, seconds_left(self.deadline)), check=False,
        )
        return result.returncode == 0


def write_private(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, "w", encoding="ascii") as stream:
        stream.write(data)


def known_host_pin(target, args, directory, deadline):
    if not args.pin_key:
        return {}
    lines = args.pin_key.read_text(encoding="ascii").strip().splitlines()
    fields = lines[0].split(maxsplit=2) if len(lines) == 1 else []
    if (len(fields) < 2 or not re.fullmatch(r"(ssh|ecdsa|sk)-[A-Za-z0-9@._+-]+", fields[0])
            or not re.fullmatch(r"[A-Za-z0-9+/]+={0,2}", fields[1])):
        raise Stop("trust", "candidate must be a single OpenSSH public host key")
    candidate = f"{fields[0]} {fields[1]}\n"
    check = subprocess.run(
        [KEYGEN, "-E", "sha256", "-lf", "-"], input=candidate.encode("ascii"),
        capture_output=True, timeout=min(5, seconds_left(deadline)), check=False,
    )
    fingerprint = check.stdout.split()
    if check.returncode or len(fingerprint) < 2 or fingerprint[1].decode() != args.fingerprint:
        raise Stop("trust", "candidate does not match the independently verified fingerprint")
    host, port = target.endpoint["host"], target.endpoint["port"]
    token = target.effective.get("hostkeyalias") or (host if port == 22 else f"[{host}]:{port}")
    if not re.fullmatch(r"[A-Za-z0-9_.:\[\]%-]+", token) or "%" in token:
        raise Stop("trust", "unable to pin the effective host-key name")
    user_files = shlex.split(target.effective.get("userknownhostsfile", ""))
    global_files = shlex.split(target.effective.get("globalknownhostsfile", ""))
    for name in user_files + global_files:
        if name == "none":
            continue
        if not Path(name).is_absolute() or any(ch in name for ch in '"\\%$'):
            raise Stop("trust", "cannot verify the configured host-key files")
        try:
            Path(name).stat()
        except FileNotFoundError:
            continue
        probe = subprocess.run(
            [KEYGEN, "-F", token, "-f", name], stdin=subprocess.DEVNULL, capture_output=True,
            timeout=min(5, seconds_left(deadline)), check=False,
        )
        if probe.returncode == 0:
            raise Stop("trust", "host already has a trust record; use its existing strict verification")
        if probe.returncode != 1 or probe.stderr:
            raise Stop("trust", "cannot verify the configured host-key files")
    pin = directory / "known_hosts"
    write_private(pin, f"{token} {candidate}")
    return {"UserKnownHostsFile": " ".join(f'"{p}"' for p in [pin, *[n for n in user_files if n != "none"]])}


def terminate_group(process):
    if process.poll() is None:
        try:
            os.killpg(process.pid, signal.SIGTERM)
            process.wait(timeout=2)
        except ProcessLookupError:
            pass
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
    process.wait()
    # The child may have exited before its askpass descendants.
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass


def clean_lease(directory):
    for name in ("control", "lease.new", "lease.json", "known_hosts", "prompt"):
        (directory / name).unlink(missing_ok=True)
    try:
        directory.rmdir()
    except FileNotFoundError:
        pass


def watch_master(directory, deadline, argv):
    """Internal watchdog. Parent pipe EOF cancels the connection on supervisor crash."""
    if os.getpid() != os.getsid(0):
        raise Stop("login", "watchdog requires a dedicated local process group")
    process = None
    try:
        process = subprocess.Popen(
            argv, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(process.pid, flush=True)
        while process.poll() is None:
            remaining = max(0, deadline - time.monotonic())
            if remaining == 0:
                return 124
            if select.select([sys.stdin], [], [], min(0.1, remaining))[0]:
                return 0
        return process.returncode
    finally:
        if process is not None:
            # The group includes SSH and the prompt, but excludes the supervisor.
            signal.signal(signal.SIGTERM, signal.SIG_IGN)
            os.killpg(os.getpgrp(), signal.SIGTERM)
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
        clean_lease(directory)


def bootstrap(args):
    start = time.monotonic()
    task_deadline, login_deadline = start + args.task_seconds, start + args.seconds
    directory = private_directory(args.lease)
    if list(directory.iterdir()) or any(ch in str(directory) for ch in '%$"\\\r\n'):
        raise Stop("login", "use a fresh empty private lease directory")
    path, state, status = (directory / name for name in ("control", "lease.json", "prompt"))
    if len(os.fsencode(path)) > 90:
        raise Stop("login", "lease directory path is too long for an OpenSSH socket")
    process = None
    try:
        target = Target(args, login_deadline)
        askpass = Path(__file__).with_name("ssh_askpass.py").resolve()
        if sys.platform != "darwin" or not os.access(askpass, os.X_OK):
            raise Stop("gui-unavailable", "macOS askpass is unavailable; use a user-owned Terminal master")
        if (any(target.effective.get(k, "none") != "none" for k in
                ("proxyjump", "proxycommand", "knownhostscommand"))):
            raise Stop("gui-unavailable", "use a user-owned Terminal master for this SSH configuration")
        pin = known_host_pin(target, args, directory, login_deadline)
        write_private(status, "")
        argv = target.verified_argv(
            path, login_deadline,
            {"ControlMaster": "yes", "ControlPersist": "no", "BatchMode": "no",
             "ProxyCommand": "none", "SessionType": "none", "StrictHostKeyChecking": "yes",
             "VerifyHostKeyDNS": "no", "UpdateHostKeys": "no", "CheckHostIP": "no",
             "PreferredAuthentications": "password", "PasswordAuthentication": "yes",
             "PubkeyAuthentication": "no", "KbdInteractiveAuthentication": "no",
             "GSSAPIAuthentication": "no", "HostbasedAuthentication": "no",
             "PKCS11Provider": "none", "SecurityKeyProvider": "internal",
             "IdentityAgent": "none", "AddKeysToAgent": "no", "UseKeychain": "no",
             "NumberOfPasswordPrompts": "1", **pin},
            {"controlmaster": "true", "controlpersist": "no", "batchmode": "no",
             "sessiontype": "none", "proxycommand": "none", "stricthostkeychecking": "true",
             "preferredauthentications": "password", "pubkeyauthentication": "false",
             "passwordauthentication": "yes", "kbdinteractiveauthentication": "no",
             "gssapiauthentication": "no", "hostbasedauthentication": "no",
             "verifyhostkeydns": "false", "updatehostkeys": "false",
             "identityagent": "none", "pkcs11provider": "none", "numberofpasswordprompts": "1"},
        )
        env = {**os.environ, "SSH_ASKPASS": str(askpass), "SSH_ASKPASS_REQUIRE": "force",
               "SSH_OPS_PROMPT_STATUS": str(status),
               "SSH_OPS_PROMPT_TARGET": "{user}@{host}:{port}".format(**target.endpoint),
               "SSH_OPS_PROMPT_SECONDS": str(max(1, int(seconds_left(login_deadline))))}
        process = subprocess.Popen(
            [sys.executable, str(Path(__file__).resolve()), "_watch", str(directory), str(task_deadline),
             *argv, "--", target.selector],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            env=env, start_new_session=True,
        )
        if not select.select([process.stdout], [], [], seconds_left(login_deadline))[0]:
            raise TimeoutError
        try:
            ssh_pid = int(process.stdout.readline(32))
        except ValueError:
            raise Stop("login", "SSH lease process failed to start") from None
        while not path.is_socket():
            if process.poll() is not None:
                raise Stop("login", "SSH stopped before authentication completed; check host trust and credentials")
            try:
                prompt = status.read_text(encoding="ascii").strip()
            except FileNotFoundError:
                raise Stop("login", "SSH stopped before authentication completed; check host trust and credentials") from None
            if prompt == "unavailable":
                raise Stop("gui-unavailable", "masked window cannot open; use a user-owned Terminal master")
            if prompt in ("canceled", "timeout", "invalid"):
                raise Stop("login", f"password prompt {prompt}")
            time.sleep(min(0.05, seconds_left(login_deadline)))
        master = Master(target, path, login_deadline)
        identity = master.identity()
        if identity[2] != ssh_pid:
            raise Stop("master", "controller does not belong to this supervisor")
        binding = {"identity": identity, "endpoint": target.endpoint, "target": target.selector,
                   "config": str(target.config or ""), "deadline": task_deadline}
        # Publish a complete lease before announcing readiness.
        write_private(directory / "lease.new", json.dumps(binding))
        (directory / "lease.new").rename(state)
        emit({"status": "ready", "socket": str(path), **target.endpoint})
        if process.wait(timeout=max(0, task_deadline - time.monotonic()) + 3) == 124:
            emit({"status": "expired", "phase": "master"})
    except (TimeoutError, subprocess.TimeoutExpired):
        raise Stop("login", "login deadline elapsed") from None
    finally:
        if process is not None:
            process.stdin.close()
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                pass
            finally:
                terminate_group(process)
                process.stdout.close()
        clean_lease(directory)


def capture_command(argv, deadline):
    output = {"stdout": bytearray(), "stderr": bytearray()}
    truncated = {name: False for name in output}
    with subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE) as process, selectors.DefaultSelector() as selector:
        selector.register(process.stdout, selectors.EVENT_READ, "stdout")
        selector.register(process.stderr, selectors.EVENT_READ, "stderr")
        try:
            while selector.get_map():
                events = selector.select(seconds_left(deadline))
                if not events:
                    raise TimeoutError
                for key, _ in events:
                    block = os.read(key.fd, CHUNK)
                    if not block:
                        selector.unregister(key.fileobj)
                        continue
                    data = output[key.data]
                    remaining = OUTPUT_LIMIT - len(data)
                    data.extend(block[:remaining])
                    truncated[key.data] |= len(block) > remaining
            ssh_code = process.wait(timeout=seconds_left(deadline))
        except (TimeoutError, subprocess.TimeoutExpired):
            process.kill()
            process.wait()
            ssh_code = None
        finally:
            if process.poll() is None:
                process.kill()
    return {
        "status": "unknown" if ssh_code is None or ssh_code == 255 or ssh_code < 0
        else ("ok" if ssh_code == 0 else "remote-nonzero"),
        "ssh_exit_code": ssh_code,
        "truncated": truncated,
        **{name: data.decode("utf-8", errors="replace") for name, data in output.items()},
    }


@contextmanager
def remote_stream(master, command):
    process = subprocess.Popen(master.command(command), stdin=subprocess.DEVNULL,
                               stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    expired = threading.Event()

    def stop():
        expired.set()
        process.kill()

    timer = threading.Timer(max(0, master.deadline - time.monotonic()), stop)
    timer.start()
    try:
        yield process.stdout
        if process.wait(timeout=seconds_left(master.deadline)):
            raise Stop("transfer", "remote probe or transfer failed")
    except (TimeoutError, subprocess.TimeoutExpired):
        raise Stop("transfer", "transfer deadline elapsed") from None
    except Stop:
        if expired.is_set():
            raise Stop("transfer", "transfer deadline elapsed") from None
        raise
    finally:
        timer.cancel()
        if process.poll() is None:
            process.kill()
        process.wait()
        process.stdout.close()
        timer.join()


def absolute_remote(path):
    if not path or not path.startswith("/") or any(ord(c) < 32 or ord(c) == 127 for c in path):
        raise Stop("source", "expected an absolute remote path without control characters")
    if path != "/" and any(part in ("", ".", "..") for part in path.split("/")[1:]):
        raise Stop("source", "use the canonical remote path")
    return path


def destination_name(name):
    if not name or name in (".", "..") or "/" in name or "\x00" in name:
        raise Stop("destination", "expected a single new local basename")
    return name


def copy_bytes(source, sink, count=None):
    digest, size = hashlib.sha256(), 0
    while count is None or size < count:
        block = source.read(CHUNK if count is None else min(CHUNK, count - size))
        if not block:
            if count is not None:
                raise Stop("integrity", "short framed file")
            break
        sink.write(block)
        digest.update(block)
        size += len(block)
    return size, digest.hexdigest()


def download_file(master, identity, remote, parent, name):
    folder, base = remote.rsplit("/", 1)
    if not base:
        raise Stop("source", "expected a regular file path")
    folder = folder or "/"
    quoted_dir, file_arg = shlex.quote(folder), shlex.quote("./" + base)
    preflight = (f"cd -P {quoted_dir} && [ \"$(pwd -P)\" = {quoted_dir} ] && "
                 f"[ ! -L {file_arg} ] && [ -f {file_arg} ] && [ -r {file_arg} ]")
    fd, temporary = tempfile.mkstemp(prefix=".ssh-file-", dir=parent)
    try:
        with os.fdopen(fd, "wb") as sink:
            with remote_stream(master, f"{preflight} && cat < {file_arg}") as source:
                size, actual = copy_bytes(source, sink)
        with remote_stream(master, f"{preflight} && sha256sum < {file_arg}") as source:
            result = source.read(72)
            if not re.fullmatch(rb"[0-9a-f]{64}  -\n", result) or source.read(1):
                raise Stop("integrity", "expected exactly one valid remote SHA-256 digest")
        if actual != result[:64].decode():
            raise Stop("integrity", "single-file SHA-256 mismatch")
        master.require_same(identity)
        try:
            os.link(temporary, parent / name, follow_symlinks=False)
        except OSError:
            raise Stop("install", "exclusive file install failed") from None
        return {"status": "ok", "path": str(parent / name), "bytes": size, "sha256": actual, "mode": "0600"}
    finally:
        Path(temporary).unlink(missing_ok=True)


def unique_object(pairs):
    result = dict(pairs)
    if len(result) != len(pairs):
        raise ValueError("duplicate field")
    return result


def frame(line, manifest):
    if len(line) > HEADER_LIMIT or not line.endswith(b"\n"):
        raise Stop("integrity", "directory frame exceeded header limit or is truncated")
    try:
        value = json.loads(line.decode("utf-8"), object_pairs_hook=unique_object)
        path = value["path"]
        kind = value["type"]
        if not isinstance(path, list):
            raise ValueError
        for item in path:
            destination_name(item)
            item.encode("utf-8")
        fields = {"type", "path"}
        if kind == "file":
            fields.add("size")
            if type(value["size"]) is not int or value["size"] < 0 or not path:
                raise ValueError
            if manifest:
                fields.add("sha256")
                if not DIGEST.fullmatch(value["sha256"]):
                    raise ValueError
        elif kind != "dir":
            raise ValueError
        if set(value) != fields:
            raise ValueError
    except (AttributeError, KeyError, ValueError, TypeError, Stop):
        raise Stop("integrity", "invalid directory frame") from None
    return tuple(path), value


@contextmanager
def local_dir(root, parts):
    fd = os.dup(root)
    try:
        for name in parts:
            child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        yield fd
    finally:
        os.close(fd)


def directory_entries(stream, *, expected=None, local=None):
    manifest = expected is None
    found = {}
    while line := stream.readline(HEADER_LIMIT + 1):
        path, value = frame(line, manifest)
        is_dir = value["type"] == "dir"
        if path in found or (path and found.get(path[:-1]) != ()):
            raise Stop("integrity", "duplicate path or missing directory parent")
        entry = () if is_dir else (value["size"], value.get("sha256"))
        if not manifest:
            if path not in expected or (not is_dir and (not expected[path] or expected[path][0] != value["size"])):
                raise Stop("integrity", "framed entry differs from the preflight manifest")
            if path:
                with local_dir(local, path[:-1]) as parent:
                    if is_dir:
                        os.mkdir(path[-1], 0o700, dir_fd=parent)
                    else:
                        fd = os.open(path[-1], os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                                     0o600, dir_fd=parent)
                        with os.fdopen(fd, "wb") as sink:
                            entry = copy_bytes(stream, sink, value["size"])
            if entry != expected[path]:
                raise Stop("integrity", "directory entry size or SHA-256 mismatch")
        found[path] = entry
    if found.get(()) != () or (not manifest and found != expected):
        raise Stop("integrity", "directory stream is incomplete")
    return found


def exclusive_rename(parent, temporary, name):
    if sys.platform != "darwin":
        raise Stop("install", "macOS exclusive rename is unavailable")
    try:
        rename = ctypes.CDLL(None, use_errno=True).renameatx_np
    except AttributeError:
        raise Stop("install", "macOS exclusive rename is unavailable") from None
    rename.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
    rename.restype = ctypes.c_int
    rename_exclusive = 0x00000004
    if rename(parent, os.fsencode(temporary), parent, os.fsencode(name), rename_exclusive):
        raise Stop("install", "exclusive directory install failed")


def download_directory(master, identity, remote, parent, name):
    walker = Path(__file__).with_name("ssh_directory.py").read_text(encoding="utf-8")
    prefix = "python3 -I -c " + shlex.quote(walker)

    def remote_mode(mode):
        return remote_stream(master, f"{prefix} {mode} {shlex.quote(remote)}")

    with remote_mode("probe") as stream:
        if stream.read(22) != b"ssh-ops-directory-v1\n" or stream.read(1):
            raise Stop("source", "remote Python capability probe failed")
    with remote_mode("manifest") as stream:
        before = directory_entries(stream)
    master.require_same(identity)
    parent_fd = os.open(parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    stage = None
    try:
        stage = Path(tempfile.mkdtemp(prefix=".ssh-tree-", dir=parent))
        with local_dir(parent_fd, [stage.name]) as local:
            with remote_mode("data") as stream:
                try:
                    observed = directory_entries(stream, expected=before, local=local)
                except FileExistsError:
                    raise Stop("destination", "local filesystem name collision") from None
        with remote_mode("manifest") as stream:
            after = directory_entries(stream)
        if before != after:
            raise Stop("integrity", "remote directory changed during transfer")
        master.require_same(identity)
        exclusive_rename(parent_fd, stage.name, name)
        stage = None
    finally:
        try:
            if stage is not None:
                shutil.rmtree(stage)
        finally:
            os.close(parent_fd)
    files = [entry for entry in observed.values() if entry]
    return {"status": "ok", "path": str(parent / name), "files": len(files),
            "bytes": sum(size for size, _ in files), "verified": "sha256"}


@contextmanager
def task_binding(directory):
    if directory is None:
        yield None
        return
    directory = private_directory(directory)
    fd = os.open(directory / "lease.json", os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(fd, encoding="ascii") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise Stop("master", "another operation is using this task lease") from None
        binding = json.load(stream)
        yield binding


def run_operation(args):
    with task_binding(args.lease) as binding:
        return run_bound_operation(args, binding)


def run_bound_operation(args, binding):
    deadline = time.monotonic() + args.seconds
    target = Target(args, deadline)
    if binding:
        if (binding["endpoint"] != target.endpoint or binding["target"] != target.selector
                or binding["config"] != str(target.config or "")):
            raise Stop("master", "lease does not belong to the approved target")
        deadline = min(deadline, binding["deadline"])
        path = args.lease / "control"
    else:
        path = args.socket
    master = Master(target, path, deadline)
    identity = master.identity()
    if binding and tuple(binding["identity"]) != identity:
        raise Stop("master", "lease controller identity changed")
    master.bound_identity = identity
    try:
        if args.operation == "login-check":
            result = {"status": "ok", **target.endpoint}
        elif args.operation == "exec":
            if not args.command or "\x00" in args.command:
                raise Stop("command", "a single approved remote command is required")
            result = capture_command(master.command(args.command), deadline)
            if result["status"] != "unknown":
                try:
                    master.require_same(identity)
                except (Stop, TimeoutError, subprocess.TimeoutExpired):
                    result["status"] = "unknown"
        else:
            if args.remote is None or args.parent is None or args.name is None:
                raise Stop("download", "specify the approved source, local parent directory and new name")
            parent = private_directory(args.parent)
            name = destination_name(args.name)
            if os.path.lexists(parent / name):
                raise Stop("destination", "the final path already exists")
            remote = absolute_remote(args.remote)
            transfer = download_file if args.operation == "download-file" else download_directory
            result = transfer(master, identity, remote, parent, name)
        return result
    finally:
        if binding:
            # A separate short cleanup window also applies when the operation timed out.
            master.deadline = time.monotonic() + 5
            try:
                closed = master.close(identity)
            except (Stop, OSError, TimeoutError, subprocess.TimeoutExpired):
                closed = False
            if not closed and path.exists():
                emit({"status": "pending", "phase": "cleanup", "reason": "await supervisor termination"})


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    inspect = commands.add_parser("inspect", help="resolve a target without connecting")
    connect = commands.add_parser("bootstrap", help="supervise one new password-authenticated master")
    run = commands.add_parser("run", help="perform one authorized operation via the exact socket")
    for sub in (inspect, connect, run):
        sub.add_argument("--target", required=True)
        sub.add_argument("-F", "--config", type=Path)
    for sub in (connect, run):
        sub.add_argument("--expect", nargs=3, required=True, metavar=("USER", "HOST", "PORT"))
        sub.add_argument("--seconds", type=int)
    connect.add_argument("--lease", required=True, type=Path)
    connect.add_argument("--task-seconds", type=int, default=900)
    connect.add_argument("--pin-key", type=Path)
    connect.add_argument("--fingerprint")
    connection = run.add_mutually_exclusive_group(required=True)
    connection.add_argument("--lease", type=Path)
    connection.add_argument("--socket", type=Path)
    run.add_argument("--command")
    run.add_argument("--remote")
    run.add_argument("--parent", type=Path)
    run.add_argument("--name")
    run.add_argument("operation", choices=("login-check", "exec", "download-file", "download-directory"))
    args = parser.parse_args(argv)
    if args.action == "bootstrap":
        args.seconds = 90 if args.seconds is None else args.seconds
        if not 0 < args.seconds <= args.task_seconds <= 1800:
            parser.error("login and task deadlines must be positive and task at most 1800 seconds")
        if bool(args.pin_key) != bool(args.fingerprint):
            parser.error("a first-use public key and its independently verified fingerprint are both required")
    if args.action == "run":
        if args.seconds is None:
            args.seconds = 600 if args.operation.startswith("download-") else 120
        if not 0 < args.seconds <= 1800:
            parser.error("operation deadline must be between 1 and 1800 seconds")
    return args


def interrupt(_signum, _frame):
    raise KeyboardInterrupt


def main():
    signal.signal(signal.SIGTERM, interrupt)
    if sys.argv[1:2] == ["_watch"]:
        if len(sys.argv) < 5 or sys.argv[4] != SSH:
            return 2
        return watch_master(private_directory(Path(sys.argv[2])), float(sys.argv[3]), sys.argv[4:])
    args = parse_args()
    try:
        if args.action == "inspect":
            target = Target(args, time.monotonic() + 15)
            emit({**target.endpoint, "target": target.selector, "config": str(target.config or "default")})
        elif args.action == "bootstrap":
            bootstrap(args)
        else:
            result = run_operation(args)
            emit(result)
            return 0 if result["status"] == "ok" else 1
    except Stop as exc:
        emit({"status": "stopped", "phase": exc.phase, "reason": str(exc)})
        return 1
    except (TimeoutError, subprocess.TimeoutExpired):
        emit({"status": "stopped", "phase": "preflight", "reason": "deadline elapsed"})
        return 1
    except (OSError, ValueError, KeyError, TypeError):
        emit({"status": "stopped", "phase": "local", "reason": "required local path, permission or data is unavailable"})
        return 1
    except KeyboardInterrupt:
        emit({"status": "stopped", "phase": "canceled", "reason": "operation canceled; a dispatched command may have run"})
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())
