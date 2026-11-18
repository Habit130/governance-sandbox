# Build and verification

The commands, CI and Actions secrets that a Builder runs and checks, and that a Planner
draws on to write a ticket's Verification. The generator wrote this file at Initialize from
what it ran. It is repository-owned, kept current by this repository's own PRs, and it sits
under `docs/agents/`, a sensitive path with a medium floor, so a PR that edits it is at
least medium.

## Commands

Python's standard library only: no package install, no service, no network.

| Purpose | Command |
| --- | --- |
| Run the tests | `python3 -m unittest discover -s tests -v` |

At Initialize this command was run on `20cd58f` with Python 3.9.6 and works: 3 tests OK.
No command failed.

## CI

- `.github/workflows/ci.yml` (`ci`): triggered on `pull_request` with no path filter; one
  job, `test`, which checks out the PR and runs the test command above. `test` is a required
  check.
- `.github/workflows/governance-gate.yml` and `.github/workflows/merge-watch.yml`: the
  governance gate and Merge watch.
- No workflow runs product build or tests on a push to `main`, so there is no default-branch
  product verification; after-merge product smoke is the test command above, run locally on
  the exact merged commit.

## Actions secrets

CI uses no Actions secret.

Only habit writes Actions secrets (`AGENTS.md`, Secrets).
