"""Emit a manifest or framed data for one absolute, no-follow directory tree."""

import hashlib
import json
import os
import stat
import sys
from contextlib import ExitStack, contextmanager

HEADER_LIMIT = 65536
CHUNK = 65536


def identity(info):
    return (info.st_dev, info.st_ino, info.st_mode, info.st_size,
            info.st_mtime_ns, info.st_ctime_ns)


@contextmanager
def open_entry(parent, name, is_dir, *, stable_contents=True):
    before = os.stat(name, dir_fd=parent, follow_symlinks=False)
    expected = stat.S_ISDIR if is_dir else stat.S_ISREG
    if not expected(before.st_mode):
        raise ValueError("unsupported source entry")
    flags = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK
    if is_dir:
        flags |= os.O_DIRECTORY
    fd = os.open(name, flags, dir_fd=parent)
    try:
        signature = identity(before)
        if identity(os.fstat(fd)) != signature:
            raise ValueError("source replaced during open")
        yield fd, before
        named = os.stat(name, dir_fd=parent, follow_symlinks=False)
        width = len(signature) if stable_contents else 3
        if any(identity(info)[:width] != signature[:width] for info in (os.fstat(fd), named)):
            raise ValueError("source changed during read")
    finally:
        os.close(fd)


def components(path):
    if path == "/":
        return []
    parts = path.split("/")
    if not path.startswith("/") or any(not p or p in (".", "..") or "\x00" in p for p in parts[1:]):
        raise ValueError("expected a canonical absolute path")
    for part in parts[1:]:
        part.encode("utf-8")
    return parts[1:]


@contextmanager
def source_root(parts):
    with ExitStack() as stack:
        fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
        stack.callback(os.close, fd)
        for index, part in enumerate(parts):
            fd, _ = stack.enter_context(open_entry(
                fd, part, True, stable_contents=(index == len(parts) - 1),
            ))
        yield fd


def emit(out, record):
    header = json.dumps(record, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    if len(header) >= HEADER_LIMIT:
        raise ValueError("source path exceeds header limit")
    out.write(header + b"\n")


def walk(fd, path, out, manifest):
    emit(out, {"type": "dir", "path": path})
    for name in sorted(os.listdir(fd)):
        name.encode("utf-8")
        child = [*path, name]
        info = os.stat(name, dir_fd=fd, follow_symlinks=False)
        if stat.S_ISDIR(info.st_mode):
            with open_entry(fd, name, True) as (child_fd, _):
                walk(child_fd, child, out, manifest)
            continue
        with open_entry(fd, name, False) as (file_fd, opened):
            record = {"type": "file", "path": child, "size": opened.st_size}
            digest = hashlib.sha256()
            if not manifest:
                emit(out, record)
            remaining = opened.st_size
            while remaining:
                block = os.read(file_fd, min(CHUNK, remaining))
                if not block:
                    raise ValueError("short source file")
                if manifest:
                    digest.update(block)
                else:
                    out.write(block)
                remaining -= len(block)
            if os.read(file_fd, 1):
                raise ValueError("source grew during read")
            if manifest:
                emit(out, {**record, "sha256": digest.hexdigest()})


def main(mode, path):
    if mode not in ("probe", "manifest", "data"):
        raise ValueError("unsupported mode")
    if (not {os.open, os.stat} <= os.supports_dir_fd
            or os.stat not in os.supports_follow_symlinks
            or os.listdir not in os.supports_fd
            or not hasattr(os, "O_NOFOLLOW") or not hasattr(os, "O_DIRECTORY")):
        raise ValueError("descriptor-relative reads are unavailable")
    with source_root(components(path)) as fd:
        if mode == "probe":
            print("ssh-ops-directory-v1")
        else:
            before = identity(os.fstat(fd))
            walk(fd, [], sys.stdout.buffer, mode == "manifest")
            if identity(os.fstat(fd)) != before:
                raise ValueError("root directory changed during read")


if __name__ == "__main__":
    try:
        main(*sys.argv[1:])
    except (OSError, ValueError, TypeError, RecursionError):
        sys.exit("directory source, capability or consistency check failed")
