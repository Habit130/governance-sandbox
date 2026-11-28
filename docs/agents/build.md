# Build and verification

The commands, CI and Actions secrets that a Builder runs and checks, and that a Planner
draws on to write a ticket's Verification. The generator wrote this file at Initialize from
what it ran. It is repository-owned, kept current by this repository's own PRs, and it sits
under `docs/agents/`, a sensitive path with a medium floor, so a PR that edits it is at
least medium.

## Commands

There is no build step and no dependency to install. Run from the repository root with
`python3` and its standard library; no service and no network are needed.

| Purpose | Command |
| --- | --- |
| Test | `python3 -m unittest discover -s tests -v` |

At Initialize the generator ran it at `2d6361a0d86ec36d7aac87a71cdb3d116ecefc28` on
Python 3.9.6: it works ("Ran 3 tests", "OK", exit 0). No command failed.

`scripts/release.sh` is not a build or test command: habit runs it after a release PR
merges, and no agent runs it.

## CI

- `.github/workflows/ci.yml` (`ci`): trigger `pull_request`, no path filters. One job,
  `test`, a required check, runs `python3 -m unittest discover -s tests -v`. Its checkout
  takes `pull_request`'s default ref, GitHub's test merge of the PR head into the base, so it
  covers that merge commit, not the PR head itself. When a review needs the exact head
  verified, run the command locally on that head.
- `.github/workflows/governance-gate.yml`: the `governance-gate` job judges every PR into
  `main` (`pull_request_target`), and is a required check.
- `.github/workflows/merge-watch.yml`: Merge watch, on pushes to `main` and completed
  workflow runs there; a governance audit, not product verification.

No product build or test job runs on the default branch: `ci` runs only on PRs. Product
smoke after a merge is therefore the test command above, run locally on the exact squash
commit (`builder.md`, After merge).

## Actions secrets

CI uses no Actions secret.

For the owner action follow `AGENTS.md`, Secrets. Use the ticket fields from
`planner.md`, Tickets.
