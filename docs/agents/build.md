# Build and verification

The commands, CI and Actions secrets that a Builder runs and checks, and that a Planner
draws on to write a ticket's Verification. The generator wrote this file at Initialize from
what it ran. It is repository-owned, kept current by this repository's own PRs, and it sits
under `docs/agents/`, a sensitive path with a medium floor, so a PR that edits it is at
least medium.

## Commands

Run from the repository root. There is no build step and nothing to install: the tests use
only Python's standard library and need no network or service.

| Purpose | Command |
| --- | --- |
| Unit tests | `python3 -m unittest discover -s tests -v` |

At Initialize (#109) this command worked on `20cd58f4e40322c0a497515b02e3679fffe3e0fc` with
local Python 3.9.6: exit code 0, `Ran 3 tests`, `OK`. That was an earlier baseline run, not
the smoke of any later merged commit.

## CI

- `.github/workflows/ci.yml`, job `test` (check name `test`): runs the unit-test command
  above on `ubuntu-24.04` with the runner's `python3`. It is triggered by `pull_request`
  only, with no path or branch filter, so it runs on every PR. It has no `push` trigger:
  no workflow runs this job on `main` after a merge.
- `test` is the required check named in `.github/governance/record.yml`, beside the fixed
  governance gate.
- The governance workflows (`governance-gate.yml`, `merge-watch.yml`) are fixed content and
  audit process, not the product.

## After-merge product smoke

Because no product job runs on `main`, the after-merge product smoke is local: on the exact
merged squash commit of `main`, run `python3 -m unittest discover -s tests -v`. It passes
only when the three unit tests in `tests/` run, the result is `OK` and the exit code is 0
(`Ran 3 tests`, `OK`). A different test count, a failure or an error fails the smoke. The
governance gate, Merge watch and PR CI do not substitute for it.

## Actions secrets

CI uses no Actions secret, `GITHUB_TOKEN` aside.

Only habit writes Actions secrets (`AGENTS.md`, Secrets).
