---
name: ssh-ops
description: "Download one explicitly authorized remote file on macOS through a user-authenticated OpenSSH master, using one-shot Codex permissions for its socket and local destination."
complexity: high
risk_profile:
  - ambiguity_sensitive
  - external_tooling
use_when:
  - "The user requests one remote-to-local file download through an authorized existing SSH master."
do_not_use_when:
  - "The task needs uploads, arbitrary remote commands, SSH authentication, changes to socket permissions, or a permanent permission profile."
inputs:
  - "Authorized SSH destination, its trusted configuration source, and the dedicated socket that belongs to that master."
  - "One absolute remote file path and an authorized local destination."
outputs:
  - "A verified local copy with mode 0600, or the phase and reason the transfer stopped."
---

# Purpose

Download a single authorized remote file on demand. Reuse a master the user has already authenticated. Apply narrowly scoped permissions to this operation.

# Trigger / When to use

Use for a single remote-to-local download in a macOS Codex environment that can enforce a one-shot sandbox. The user can make the request after opening Codex. For uploads, interactive shells, credential setup, or a general SSH command runner, use the appropriate separate workflow.

# Inputs

- Exact user-authorized SSH destination and absolute remote file path. Identify the default SSH config or the exact trusted config used with `-F`.
- Dedicated socket for that destination and account. The user establishes the socket-to-destination mapping from the terminal that created the master. `-O check` checks liveness and returns a PID. A PID alone does not establish the remote identity.
- Existing private local destination directory and one new filename within it. Canonicalize the directory, verify that it is user-owned, and scope permission to the resolved path. If the user only asks for a temporary destination, choose and disclose a new private temporary directory.
- The platform's approval and enforcement mechanism for the one-shot operation, where required by the active policy.

# Process

1. Confirm the authorized file and destination. Use explicit paths, validate the destination as an SSH target, and pass local arguments as an argument array with `--` before the destination. OpenSSH sends the remote command as shell text. Quote the remote file path as one POSIX shell argument and hold the remote operation fixed. Refuse broad selectors, control characters, and paths that cannot be safely addressed.
2. If the master is missing, ask the user to establish it in their terminal and provide the matching socket. The user handles passwords and keys. Keep the trusted config source and destination identical from check through transfer. Inspect relevant configuration and includes before use. If it can run a local executable during configuration evaluation, such as a matching `Match exec`, choose an equivalent trusted input without that hook or stop.
3. Resolve a one-shot macOS sandbox through the supported Codex mechanism. Use a read-only base, only the exact dedicated Unix socket, write access only to the approved destination directory, and direct network off. Preserve managed restrictions. If the current tool cannot enforce this scope, return the specific blocker.
4. Inside that sandbox, run `ssh -S SOCKET -O check DESTINATION` with the matching config and a bounded timeout. Record the expected master during this operation. Use the same socket and config for the remote readability check, file read, and remote SHA-256. Use `-nT`, `-o ControlMaster=no`, `-o BatchMode=yes`, and `-o ProxyCommand=/usr/bin/false`. Set `ClearAllForwardings=yes`, `ForwardAgent=no`, `ForwardX11=no`, and `PermitLocalCommand=no` from the command line. Apply these to every client invocation, and keep each phase noninteractive and time-bounded.
5. Confirm the exact remote path is readable and refers to a regular file. Resolve links against the authorized scope before reading if links are involved. Open a new, exclusive temporary file in the destination directory with mode `0600`. Stream the file bytes there. Keep transfer bytes and raw credential-bearing diagnostics out of the response.
6. After a successful transfer, verify the local SHA-256 against the remote SHA-256 observed over the same master. Ensure the master still matches the operation's initial check. Install the local file atomically without overwriting an existing path. For example, create a same-directory hard link to the verified temporary file with exclusive final-name semantics, then unlink only that temporary name. A collision or unsupported install method stops delivery and preserves the existing path.

# Examples

- Positive: the user requests one specified CSV, provides a live master, and authorizes an empty filename in a private destination. The request succeeds after a digest match and a no-overwrite install.
- Negative: the master becomes unavailable and a key is present in `ssh-agent`. Stop and report the socket failure. The agent does not open a replacement connection.

# Outputs

Report the destination path, byte count, SHA-256 match, and local mode on success. If the operation stops, report whether the blocker is the master, permissions, remote source, local destination, transfer, integrity, or file install.

# Boundaries

- The only remote actions are non-mutating probes, reading the authorized file, and calculating its digest. The local sandbox cannot constrain what the server account could do. Server-enforced read-only access requires an appropriately restricted server-side SSH or SFTP account. This workflow uses a POSIX command-capable SSH account.
- No uploads, remote writes, credential handling, persistent configuration changes, ownership changes, automatic reconnection, or master lifecycle changes.
- An existing user authorization covers the same bounded action. Apply the host's approval mechanism if the active permissions require it. Managed denials take precedence.

# Validation

- Verify socket ownership and association with the authorized destination. Check the same master and effective destination write permission inside the sandbox running the transfer.
- Verify the remote exit status, local bytes, hash match, mode `0600`, and absence of overwrite before claiming success.
- If a prerequisite cannot be checked, mark the affected phase incomplete. Preserve the evidence already obtained. If a security boundary cannot be enforced or the socket has died, stop the transfer.

# Failure Handling

- **Missing Context:** Ask only for the missing file, approved destination, trusted config or master socket. For a missing master, the user may supply a new one for a later attempt.
- **Ambiguous Requirement:** Resolve the exact remote file and local final name before making remote or local changes. Leave unrelated files untouched.
- **Execution Limitation:** On permission denial, timeout, hash mismatch, remote failure or local collision, report the failing phase and remove only this attempt's temporary file. A verified final path must never point to incomplete content. A rerun uses a new temporary file and verifies the inputs again.

# Local references

- [examples.md](examples.md) shows both SSH configuration entrances, password and key scenarios, bounded commands, and failure outcomes.
