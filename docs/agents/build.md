# Build and verification

The commands, CI and Actions secrets that a Builder runs and checks, and that a Planner
draws on to write a ticket's Verification. The generator wrote this file at Initialize from
what it ran. It is repository-owned, kept current by this repository's own PRs, and it sits
under `docs/agents/`, a sensitive path with a medium floor, so a PR that edits it is at
least medium.

## Commands

| Purpose | Command | Result |
| --- | --- | --- |
| Test | `python3 -m unittest discover -s tests -v` | Working: 3 tests pass. Needs only Python 3 and no network. |

There is no build step and no package install.

## CI

One workflow, `.github/workflows/ci.yml`, runs on every pull request with no path filter. Its
one job, `test`, runs the test command above on `ubuntu-24.04`, and it is the required check.
It does not run on pushes to the default branch, so the default branch has no push-triggered
CI run to serve as a smoke check.

## Actions secrets

CI uses no Actions secret.

Only habit writes Actions secrets (`AGENTS.md`, Secrets).
