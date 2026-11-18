# Build and verification

The commands, CI and Actions secrets that a Builder runs and checks, and that a Planner
draws on to write a ticket's Verification. The generator wrote this file at Initialize from
what it ran. It is repository-owned, kept current by this repository's own PRs, and it sits
under `docs/agents/`, a sensitive path with a medium floor, so a PR that edits it is at
least medium.

## Commands

Run from the repository root. They need only Python 3's standard library: no package
install, service or network.

| Purpose | Command | Result at Initialize |
| --- | --- | --- |
| Test (the `test` CI job's command) | `python3 -m unittest discover -s tests -v` | works: 3 tests, OK, on `20cd58f4e403` |

No agent runs `scripts/release.sh`: habit runs it after a release PR merges (`AGENTS.md`,
This repository).

## CI

- `.github/workflows/ci.yml` (workflow `ci`): triggered on `pull_request` only, with no path
  or branch filter. One job, `test`, runs the test command above on Ubuntu 24.04 with a
  5-minute timeout. `test` is a required check.
- Nothing runs on a push to `main`, so there is no default-branch product run. Product smoke
  after a merge is the test command above, run locally on the exact merged commit; success is
  exit code 0 with every test OK.
- The governance workflows (`governance-gate.yml`, `merge-watch.yml`) are governance audits,
  not product verification.

## Actions secrets

CI uses no Actions secret.

Only habit writes Actions secrets (`AGENTS.md`, Secrets).
