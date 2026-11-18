# Build and verification

The commands, CI and Actions secrets that a Builder runs and checks, and that a Planner
draws on to write a ticket's Verification. The generator wrote this file at Initialize from
what it ran. It is repository-owned, kept current by this repository's own PRs, and it sits
under `docs/agents/`, a sensitive path with a medium floor, so a PR that edits it is at
least medium.

## Commands

Run from the repository root. The command needs `python3` with its standard library only.
There is nothing to install, and it uses no network.

| Purpose | Command | Status at Initialize |
| --- | --- | --- |
| Unit tests | `python3 -m unittest discover -s tests -v` | Works. It ran 3 tests, all OK, and exited 0 (2026-11-18, at `20cd58f`). |

There is no build step. `scripts/release.sh` is not a build or test command. It tags and
pushes a release, and only habit runs it, after a release PR merges. Never run it as
verification or smoke.

## CI

- `.github/workflows/ci.yml` (`ci`) has one job, `test`, which runs the unit test command
  above on `ubuntu-24.04`. It is triggered on every `pull_request`, with no path or branch
  filter. It is the confirmed required check.
- No workflow runs product build or test on a push to the default branch. So the product
  smoke after a merge is the local unit test command, run on the exact merged commit.
- The governance workflows (`governance-gate`, `merge-watch`) are audits. They are not
  product smoke.

## Actions secrets

CI uses no Actions secret.

Only habit writes Actions secrets (`AGENTS.md`, Secrets).
