# Build and verification

The commands, CI and Actions secrets that a Builder runs and checks, and that a Planner
draws on to write a ticket's Verification. The generator wrote this file at Initialize from
what it ran. It is repository-owned, kept current by this repository's own PRs, and it sits
under `docs/agents/`, a sensitive path with a medium floor, so a PR that edits it is at
least medium.

## Commands

There is no build step and no package install. Run from the repository root; no service or network is needed.

| Purpose | Command | Result at Initialize |
| --- | --- | --- |
| Test | `python3 -m unittest discover -s tests -v` | works (3 tests pass) |

## CI

`.github/workflows/ci.yml` runs on every `pull_request`, with no path or branch filter. Its one job, `test`, runs the test command above on `ubuntu-24.04` and is a required check. The workflow has no push trigger, so the default branch has no CI run after a merge.

## Actions secrets

CI uses no Actions secret.

Only habit writes Actions secrets (`AGENTS.md`, Secrets).
