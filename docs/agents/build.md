# Build and verification

The commands, CI and Actions secrets that a Builder runs and checks, and that a Planner
draws on to write a ticket's Verification. The generator wrote this file at Initialize from
what it ran. It is repository-owned, kept current by this repository's own PRs, and it sits
under `docs/agents/`, a sensitive path with a medium floor, so a PR that edits it is at
least medium.

## Commands

Standard library only: no install, no network, no service.

| Purpose | Command | Status at Initialize |
| --- | --- | --- |
| Run the tests | `python3 -m unittest discover -s tests -v` | Works: 3 tests OK at `3e195163a6a322fcebb5cadee48e7e2a16c2d311`, local Python 3.9.6 |

There is no build step.

## CI

- `.github/workflows/ci.yml`: job `test`, on `pull_request` with no filter, runs the test
  command above on `ubuntu-24.04`. It is the required check. It does not run on pushes to the
  default branch, so there is no default-branch product CI: product smoke after merge is the
  test command above, run locally on the exact squash commit (`builder.md`, After merge).
- `.github/workflows/governance-gate.yml`: job `governance-gate`, on `pull_request_target`
  into `main`; the governance gate.
- `.github/workflows/merge-watch.yml`: job `merge-watch`, on pushes to the default branch
  and workflow runs; the after-merge governance audit. Not product smoke.

## Actions secrets

CI uses no Actions secret.

Only habit writes Actions secrets (`AGENTS.md`, Secrets).
