# Plan: Git Pre-Commit Hook for Link Checking

## Task
Set up `check_links.py` as a git pre-commit hook so all links in `index.html` are automatically verified before every commit. Block commits if any links are broken or if referenced files are untracked (since untracked = 404 on GH Pages).

## Current State
- `check_links.py` exists at repo root, parses `index.html`, checks 98 local links
- Currently exits 1 only for BROKEN (missing) files; exits 0 for UNTRACKED
- No pre-commit hook exists (`.git/hooks/` has only `.sample` files)

## Implementation Steps

### Step 1: Update `check_links.py` to fail on untracked files too
Add a `--strict` flag (used by pre-commit hook) that exits 1 if ANY untracked files are found. Default behavior (no flag) stays unchanged for manual use.

Changes to `check_links.py`:
- Add `--strict` CLI argument via `sys.argv`
- When `--strict`: exit 1 if `broken > 0 OR untracked > 0`
- When not strict: exit 1 only if `broken > 0` (current behavior)

### Step 2: Create `.git/hooks/pre-commit`
Write a shell script at `.git/hooks/pre-commit` that:
- Runs `python check_links.py --strict` from repo root
- If exit code != 0, print error message and block commit
- If exit code == 0, allow commit

The hook must be executable (`chmod +x`).

### Step 3: Verify the hook works
- Run `git commit --allow-empty -m "test"` to verify hook triggers
- Confirm it passes (all links currently OK)

## Acceptance Criteria
- [ ] `check_links.py --strict` exits 1 when untracked links exist
- [ ] `.git/hooks/pre-commit` exists and is executable
- [ ] Hook blocks commits when links are broken or untracked
- [ ] Hook passes when all links are OK (current state)
- [ ] Normal `check_links.py` (no flag) behavior unchanged

## Risks
- **Windows compatibility:** Git hooks on Windows run through Git Bash. The shebang `#!/bin/sh` works. Python must be on PATH (confirmed: anaconda3 python is available).
- **Hook not shared via git:** `.git/hooks/` is local-only, not tracked. This is expected for this repo. Document in the plan file for future reference.

PLAN_READY: .omc/plans/pre-commit-hook.md
