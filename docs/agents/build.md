# Build and verification

The commands, CI and Actions secrets that a Builder runs and checks, and that a Planner
draws on to write a ticket's Verification. The generator wrote this file at Initialize from
what it ran. It is repository-owned, kept current by this repository's own PRs, and it sits
under `docs/agents/`, a sensitive path with a medium floor, so a PR that edits it is at
least medium.

## Commands

The repository has no package manifest and installs nothing. Run commands from the
repository root.

| Purpose | Command | Status |
| --- | --- | --- |
| Unit tests (Python standard library only, no install, no network) | `python3 -m unittest discover -s tests -v` | Working at Initialize: 3 tests, `OK`, exit 0 |

`scripts/release.sh <version>` tags the current commit `v<version>` and pushes the tag to
`origin`. habit runs it after a release PR merges. It is never run by an agent and is never
a verification or smoke command.

## CI

- `.github/workflows/ci.yml` (`ci`): triggered by `pull_request` only, with no path filter.
  Its one job, `test`, runs `python3 -m unittest discover -s tests -v` on the PR head, and is
  a required check.
- `.github/workflows/governance-gate.yml` and `.github/workflows/merge-watch.yml` are the
  governance audits; they are not product verification.
- No workflow runs product build or test on a push to the default branch. After-merge product
  smoke is therefore the local unit-test command above, run on the exact squash commit
  (`builder.md`, After merge).

## Actions secrets

CI uses no Actions secret.

For the owner action follow `AGENTS.md`, Secrets. Use the ticket fields from
`planner.md`, Tickets.
