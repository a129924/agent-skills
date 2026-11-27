# ssh-ops examples

Resolve the reviewed skill directory and set runner to its absolute scripts/ssh_ops.py path. The values below are illustrative.

## Resolve the destination

The user can say “登入 reports.example，帳號是 reports” or give reports@reports.example. Pass a configured alias as the target if the user uses one.

~~~bash
target='reports@reports.example'
ssh_cfg=()
# ssh_cfg=(-F '/absolute/path/to/trusted-config')
python3 "$runner" inspect --target "$target" "${ssh_cfg[@]}"
expect=(--expect reports reports.example 22)
~~~

Review the effective host, port and account. Set expect from the result even when target is an alias.

## Start the macOS masked login

Use a fresh private directory. Start the foreground supervisor in its own task session under the supported one-time network and GUI permissions, with write access to that directory. The following command is the payload for that approved invocation. If the client cannot grant the required scope, use the Terminal route.

~~~bash
lease=$(mktemp -d /private/tmp/ssh-ops.XXXXXXXX)
python3 "$runner" bootstrap --target "$target" "${ssh_cfg[@]}" \
  "${expect[@]}" --lease "$lease"
~~~

For first-use trust, get the server's public host key and independently confirm its SHA-256 fingerprint with a trusted source. Supply the one-line key using --pin-key and the trusted fingerprint using --fingerprint. A key-discovery result alone does not establish trust.

Wait for status ready and the exact socket. Keep the supervisor running while invoking the action with --lease. If the action cannot start, cancel the supervisor and check that the lease disappears. Canceling the dialog or failing authentication ends that attempt.

## Reuse a user-owned Terminal master

For key authentication, MFA, or a GUI availability blocker, the user can authenticate in their Terminal with a dedicated socket.

~~~bash
socket_dir=$(mktemp -d /private/tmp/ssh-master.XXXXXXXX)
socket="$socket_dir/control"
/usr/bin/ssh "${ssh_cfg[@]}" -S "$socket" -MNf \
  -o ControlPersist=15m -o ClearAllForwardings=yes \
  -o ForwardAgent=no -o ForwardX11=no -o PermitLocalCommand=no -- "$target"
/usr/bin/ssh "${ssh_cfg[@]}" -S "$socket" -O check -- "$target"
~~~

The user confirms the socket-to-target association and closes the master using ssh -O exit with the same settings when finished.

## Apply the per-operation sandbox

Use --lease "$lease" for a managed master. Use --socket "$socket" for a user-owned master. Set socket to the exact known path, including for the lease route.

~~~bash
connection=(--socket "$socket")
# connection=(--lease "$lease")
cmd='docker ps --format "{{.Names}}"'
operation=(python3 "$runner" run --target "$target" "${ssh_cfg[@]}" \
  "${expect[@]}" "${connection[@]}" --command "$cmd" exec)
codex sandbox --permission-profile ssh-ops-once --include-managed-config \
  -c 'permissions.ssh-ops-once.extends=":read-only"' \
  -c 'permissions.ssh-ops-once.network.enabled=false' \
  --allow-unix-socket "$socket" -- "${operation[@]}"
~~~

Use login-check to verify just the login. A generated command that starts a container needs the user's confirmation of the exact command, target and effect. A command with an unknown result may already have run. Check the remote state before seeking authorization to retry.

For downloads, add write access to the exact resolved, private local parent. This example uses a fixed illustrative path for the permission flag.

~~~bash
operation=(python3 "$runner" run --target "$target" "${ssh_cfg[@]}" \
  "${expect[@]}" "${connection[@]}" --remote /exports/reports \
  --parent /private/tmp/ssh-download-demo --name reports-copy download-directory)
codex sandbox --permission-profile ssh-ops-once --include-managed-config \
  -c 'permissions.ssh-ops-once.extends=":read-only"' \
  -c 'permissions.ssh-ops-once.network.enabled=false' \
  -c 'permissions.ssh-ops-once.filesystem={ "/private/tmp/ssh-download-demo" = "write" }' \
  --allow-unix-socket "$socket" -- "${operation[@]}"
~~~

For a single file, substitute download-file, the approved absolute source and a new basename. Single-file mode uses the physical source path, the remote POSIX shell and sha256sum. Confirm the physical path when the requested path traverses a link. Directory mode uses Python 3 and rejects links and special files.

## Outcomes

| Observation | Outcome |
| --- | --- |
| Target changed, socket missing or sandbox denial | Stop before dispatch. Cancel any unused owned supervisor. |
| GUI unavailable | The user may establish a Terminal master. |
| Prompt canceled, password wrong or host trust failed | End the attempt and clean the owned lease. |
| SSH exit 255, timeout or disconnect | Return observed SSH result and record remote completion as unknown. |
| Source changes, stream fails or destination collides | Report the phase, remove task staging and retain existing content. |
