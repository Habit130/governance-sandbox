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

Baseline: at Initialize this command was run on `20cd58f` with Python 3.9.6 and works:
3 tests OK. No command failed. This records that earlier run; it is not a result for any
later commit.

## CI

- `.github/workflows/ci.yml` (`ci`): triggered on `pull_request` with no path filter; one
  job, `test`, which checks out the PR and runs the test command above. `test` is a required
  check.
- `.github/workflows/governance-gate.yml` and `.github/workflows/merge-watch.yml`: the
  governance gate and Merge watch.
- Product CI runs only on pull requests. On a push to `main` only Merge watch runs, and it
  runs no product build or tests, so there is no default-branch product verification.

## After-merge product smoke

- **Command**: the test command above, run locally from the repository root on the exact
  squash commit the merge created on `main`.
- **Prerequisites**: `python3`, standard library only; no install.
- **Passes** only when the run reports `Ran 3 tests` and `OK`, and exits with code 0. A run
  that discovers fewer tests fails, even when it exits 0. Three is the suite's count at
  Initialize (#107); a PR that changes the count updates it here.
- The Baseline under Commands is not this smoke's result; record each smoke's own run.

## Actions secrets

CI uses no Actions secret.

Only habit writes Actions secrets (`AGENTS.md`, Secrets).
