# Build and verification

The commands, CI and Actions secrets that a Builder runs and checks, and that a Planner
draws on to write a ticket's Verification. The generator wrote this file at Initialize from
what it ran. It is repository-owned, kept current by this repository's own PRs, and it sits
under `docs/agents/`, a sensitive path with a medium floor, so a PR that edits it is at
least medium.

## Commands

Each command runs from the repository root. They need only `python3` and its standard
library: no install, no service and no network.

| Purpose | Command | Status |
| --- | --- | --- |
| Test | `python3 -m unittest discover -s tests -v` | Works: 3 tests, OK (Python 3.9.6, at Initialize) |

There is no separate build step.

## CI

- `.github/workflows/ci.yml` (`ci`): job `test`, on every `pull_request` with no branch or
  path filter. It runs the test command above. `test` is a required check. It does not run
  on pushes to the default branch, so there is no default-branch product CI; product smoke
  after a merge is the test command, run locally on the exact merged commit.
- `.github/workflows/governance-gate.yml` (`governance-gate`): on `pull_request_target` to
  `main`; the governance gate, a required check.
- `.github/workflows/merge-watch.yml` (`merge-watch`): on pushes to `main` and completed
  workflow runs on `main`; records misses. It is a governance audit, not product smoke.

## Actions secrets

CI uses no Actions secret.

Only habit writes Actions secrets (`AGENTS.md`, Secrets).
