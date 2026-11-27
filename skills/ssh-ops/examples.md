# ssh-ops examples

All host, directory and file values below are illustrative. Execute a transfer only for the file and destination authorized for that operation.

## Ask after opening the CLI

> Download the specified report at `reports.example:/exports/daily.csv` to a new file in my private temporary directory. Use the socket I created for my authenticated reports account.

The agent resolves the exact file, shows the resolved private destination, and checks access under the one-shot sandbox used for the transfer. It checks the socket before reading the file. If the existing sandbox lacks permission, this exact operation goes through Codex's available per-operation approval mechanism. Use the existing dialogue. For native-load validation, confirm that `$ssh-ops` resolves to the reviewed version in that dialogue. Stop at loading if the version cannot be verified there.

## Establish the master in the user's terminal

The same reuse procedure applies to a master authenticated with a password or a key. Any authentication prompt stays in the user's terminal.

| Configuration entrance | Password | Key |
| --- | --- | --- |
| Default SSH config | User enters password when creating the master for the configured destination. | User selects the configured identity and enters any key passphrase in the terminal. |
| Trusted `-F` file | User creates the master using the selected config and enters the password in the terminal. | User creates the master with the selected config's key and enters any key passphrase in the terminal. |

Example for a fresh private socket directory:

```bash
destination='reports.example'
ssh_cfg=()
# For an existing, trusted alternate config:
# ssh_cfg=(-F "/path/to/trusted-ssh-config")
ssh_dir=$(mktemp -d /tmp/ssh-file.XXXXXXXX) &&
  socket="$ssh_dir/control" &&
  ssh "${ssh_cfg[@]}" -S "$socket" -M -N -f -o ControlPersist=15m "$destination" &&
  ssh "${ssh_cfg[@]}" -S "$socket" -O check "$destination"
```

The user associates the socket with the selected destination and account when sharing it with Codex. For an existing socket, reuse it after confirming that association and liveness. The user closes it when finished with the same config, socket and `-O exit`.

## Apply the one-shot boundary

On macOS, a supported Codex sandbox launcher can select a named permission profile, apply managed requirements, and allow a specific Unix socket. Start the profile from `:read-only`, keep network disabled, and grant write access to the one resolved local destination directory. Define it only for the invocation. Use the host's approved launcher to apply the profile and exact socket to the bounded transfer. See [Codex CLI sandbox flags](https://learn.chatgpt.com/docs/developer-commands?surface=cli#codex-sandbox) and [permission profiles](https://learn.chatgpt.com/docs/permissions).

The following is an invocation shape with fixed, illustrative values. The bounded transfer command is the trusted local operation that implements the steps in the skill. If the installed launcher cannot enforce these arguments, stop before transfer.

```bash
codex sandbox --permission-profile ssh-file-once --include-managed-config \
  -c 'permissions.ssh-file-once.extends=":read-only"' \
  -c 'permissions.ssh-file-once.network.enabled=false' \
  -c 'permissions.ssh-file-once.filesystem={ "/private/tmp/ssh-file-demo" = "write" }' \
  --allow-unix-socket /private/tmp/ssh-master-demo/control \
  -- "${approved_transfer_argv[@]}"
```

Inside that sandbox, use the matching trusted SSH settings for every stage. The following is **runner pseudocode**. It uses an argument array locally and quotes the exact authorized remote path as one POSIX shell argument. Each checked call closes stdin, has a deadline, and stops the procedure on any error.

```text
ssh = ["/usr/bin/ssh", *ssh_cfg, "-S", socket, "-nT",
       "-o", "ControlMaster=no", "-o", "BatchMode=yes",
       "-o", "ProxyCommand=/usr/bin/false",
       "-o", "ClearAllForwardings=yes", "-o", "ForwardAgent=no",
       "-o", "ForwardX11=no", "-o", "PermitLocalCommand=no",
       "-o", "RemoteCommand=none", "-o", "SessionType=default"]
master = require_success(ssh + ["-O", "check", "--", destination], timeout=10)
path_arg = quote_one_posix_shell_argument(authorized_remote_path)
remote = ssh + ["--", destination]
require_success(remote + ["test -f " + path_arg + " && test -r " + path_arg], timeout=10)
stage = open_exclusive_private_temp_file(in=approved_local_directory, mode=0600)
try:
    require_success(remote + ["cat < " + path_arg], stdout=stage, timeout=transfer_deadline)
    digest = require_success(remote + ["sha256sum < " + path_arg], timeout=digest_deadline)
    require_same_master(ssh, destination, master, timeout=10)
    require_equal_sha256(stage, parse_one_sha256(digest))
    install_exclusively(stage, approved_final_name)
finally:
    remove_only_this_attempts_temporary_name()
```

Capture raw diagnostics privately and report only the failing phase and relevant details. File bytes flow to the open temporary file. This example uses a server with an approved `sha256sum` utility. Choose finite transfer and digest deadlines before staging and wait for the bounded client to exit before cleanup.

## Stops and outcomes

| Observation | Outcome |
| --- | --- |
| No master or sandbox denies the socket | Report the preflight blocker. Ask the user to establish a master or use the approved one-shot permission path, as applicable. |
| Master expires after the preflight | The next reuse-only command selects local `/usr/bin/false` and ends. Clean this attempt's partial file if one exists. |
| Remote path is missing, unreadable or outside the authorized scope | Report the source blocker before delivering a file. |
| Destination is unwritable or the final name already exists | Report the destination blocker. Preserve existing files. |
| Stream times out, produces a nonzero exit, or the digest differs | Remove this attempt's temporary file and report the actual failing phase. |
| SFTP-only account cannot run the needed read and digest commands | Report the unsupported server interface for this version. The account's server-side policy remains authoritative. |
