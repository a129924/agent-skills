#!/usr/bin/env bash
# Verify a pushed commit with WSL-native Git metadata and pre-commit.

set -euo pipefail

readonly PRE_COMMIT_VERSION="4.6.1"

usage() {
  cat <<'EOF'
Usage: verify-wsl-precommit.sh --repo-url URL --sha COMMIT_SHA [--cache-root PATH]

Create a temporary WSL-native worktree for COMMIT_SHA and run all pre-commit
hooks with pre-commit 4.6.1. URL must be the origin URL containing COMMIT_SHA.

Options:
  --repo-url URL      Required origin URL for the repository.
  --sha COMMIT_SHA    Required full, 40-character commit SHA.
  --cache-root PATH   Native Linux cache location. Defaults to
                      $XDG_CACHE_HOME/agent-skills-precommit, or
                      $HOME/.cache/agent-skills-precommit.
  -h, --help          Show this help text.
EOF
}

die() {
  printf 'error: %s\n' "$*" >&2
  exit 2
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || die "required command not found: $1"
}

repo_url=""
commit_sha=""
cache_root="${XDG_CACHE_HOME:-$HOME/.cache}/agent-skills-precommit"

while (($#)); do
  case "$1" in
    --repo-url)
      (($# >= 2)) || die "--repo-url requires a value"
      repo_url="$2"
      shift 2
      ;;
    --sha)
      (($# >= 2)) || die "--sha requires a value"
      commit_sha="$2"
      shift 2
      ;;
    --cache-root)
      (($# >= 2)) || die "--cache-root requires a value"
      cache_root="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown argument: $1"
      ;;
  esac
done

[[ -n "$repo_url" ]] || die "--repo-url is required"
[[ "$commit_sha" =~ ^[0-9a-fA-F]{40}$ ]] || die "--sha must be a full 40-character commit SHA"

for required_command in flock git mktemp realpath sha256sum uv; do
  require_command "$required_command"
done

mkdir -p "$cache_root"
cache_root="$(realpath -e "$cache_root")"
case "$cache_root" in
  /mnt/*)
    die "--cache-root must be on the WSL Linux filesystem, not under /mnt: $cache_root"
    ;;
esac

commit_sha="${commit_sha,,}"
repository_key="$(printf '%s' "$repo_url" | sha256sum | awk '{print $1}')"
bare_repository="$cache_root/repositories/$repository_key.git"
runs_directory="$cache_root/runs"
pre_commit_home="$cache_root/pre-commit"
lock_file="$cache_root/$repository_key.lock"

mkdir -p "$cache_root/repositories" "$runs_directory" "$pre_commit_home"

exec 9>"$lock_file"
flock 9

if [[ -e "$bare_repository" && ! -d "$bare_repository" ]]; then
  die "cache entry is not a directory: $bare_repository"
fi

if [[ ! -d "$bare_repository" ]]; then
  printf 'Creating WSL-native bare cache: %s\n' "$bare_repository"
  git clone --bare "$repo_url" "$bare_repository"
else
  cached_url="$(git -C "$bare_repository" remote get-url origin)"
  [[ "$cached_url" == "$repo_url" ]] || die "cache remote URL differs from --repo-url: $bare_repository"
fi

printf 'Fetching origin into WSL-native cache...\n'
git -C "$bare_repository" fetch --prune --tags origin \
  '+refs/heads/*:refs/remotes/origin/*'

resolved_sha="$(git -C "$bare_repository" rev-parse --verify --quiet "${commit_sha}^{commit}")" \
  || die "commit is not available from origin: $commit_sha"
[[ "$resolved_sha" == "$commit_sha" ]] || die "resolved commit does not match requested SHA: $resolved_sha"

run_directory="$(mktemp -d "$runs_directory/run.XXXXXX")"
worktree="$run_directory/repository"

cleanup() {
  local status="$1"

  if ((status == 0)); then
    if ! git -C "$bare_repository" worktree remove --force "$worktree"; then
      printf 'error: could not remove successful temporary worktree: %s\n' "$worktree" >&2
      return 1
    fi
    rmdir "$run_directory"
    return 0
  fi

  printf 'Validation failed; preserving WSL-native worktree: %s\n' "$worktree" >&2
  return "$status"
}

trap 'cleanup $?' EXIT

printf 'Creating detached worktree at %s\n' "$worktree"
git -C "$bare_repository" worktree add --detach "$worktree" "$commit_sha"

worktree_sha="$(git -C "$worktree" rev-parse HEAD)"
[[ "$worktree_sha" == "$commit_sha" ]] || die "worktree HEAD does not match requested SHA: $worktree_sha"

printf 'Running pre-commit %s for %s\n' "$PRE_COMMIT_VERSION" "$commit_sha"
export PRE_COMMIT_HOME="$pre_commit_home"
cd "$worktree"
uvx --from "pre-commit==${PRE_COMMIT_VERSION}" pre-commit run --all-files
