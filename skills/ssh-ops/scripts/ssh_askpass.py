#!/usr/bin/env python3
"""Send a single masked answer directly to OpenSSH's askpass pipe."""

import fcntl
import os
import subprocess
import sys
import time
from pathlib import Path

DIALOG = """
on run argv
    try
        set response to display dialog ("SSH 密碼 · " & item 1 of argv) ¬
            default answer "" buttons {"取消", "登入"} default button "登入" ¬
            cancel button "取消" with hidden answer giving up after (item 2 of argv as integer)
        if gave up of response then error "SSH dialog timed out" number -1712
        return text returned of response
    on error number errNumber
        if errNumber is -128 then error "SSH dialog canceled" number -128
        if errNumber is -1712 then error "SSH dialog timed out" number -1712
        error "SSH dialog unavailable" number 42
    end try
end run
"""


def set_status(path, status):
    with path.open("w", encoding="ascii") as handle:
        handle.write(status + "\n")


def claim_prompt(path):
    with path.open("r+", encoding="ascii") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        if handle.read().strip():
            return False
        handle.write("prompt\n")
        return True


def stop(path, status):
    set_status(path, status)
    # Returning failure can become an empty password in OpenSSH. Wait for the
    # supervisor to terminate the process group instead of returning an answer.
    time.sleep(1800)
    return 1


def main():
    path = Path(os.environ["SSH_OPS_PROMPT_STATUS"])
    if not claim_prompt(path):
        return stop(path, "invalid")
    try:
        result = subprocess.run(
            ["/usr/bin/osascript", "-e", DIALOG, "--", os.environ["SSH_OPS_PROMPT_TARGET"],
             os.environ["SSH_OPS_PROMPT_SECONDS"]],
            stdin=subprocess.DEVNULL, capture_output=True, check=False,
        )
    except OSError:
        return stop(path, "unavailable")
    if result.returncode != 0:
        if b"(-128)" in result.stderr:
            return stop(path, "canceled")
        if b"(-1712)" in result.stderr:
            return stop(path, "timeout")
        return stop(path, "unavailable")
    answer = result.stdout.removesuffix(b"\n")
    if not answer or any(ch in answer for ch in (b"\n", b"\r", b"\x00")):
        return stop(path, "invalid")
    set_status(path, "submitted")
    sys.stdout.buffer.write(answer + b"\n")
    sys.stdout.buffer.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
