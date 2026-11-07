# HEA milestones

This is the canonical progress tracker. Completion means the criteria below are evidenced, not merely that an agent produced files. Human data review remains with @d4rkd0s.

| Marker | Milestone | Status | Completion evidence |
| --- | --- | --- | --- |
| M0 | Definition and governance | Complete | README, AGENTS, CLAUDE, contribution rules, CC0 |
| M1 | Data contract and build | Complete | Schema, validator, deterministic bundle, integrity tests |
| M2 | Foundational dataset | Awaiting maintainer review in PR #2 | Sourced states and relationships, naming review, maintainer merge |
| M3 | Coverage expansion | Ongoing after foundation | Additional reviewed batches and explicit coverage gaps |
| M4 | Search and relationship explorer | Implemented; browser checks in progress | Search, detail, map, sources, prompt, mobile and empty-state checks |
| M5 | Public release | Pending | Green checks, Pages deployed, foundation data reviewed and merged |

## M0 · Definition
- [x] Establish descriptive purpose and scope without an inference engine.
- [x] Capture interview decisions in AGENTS.md, with CLAUDE.md pointing to it.
- [x] Set English-first, CC0, broad source eligibility, and contextual provenance.
- [x] Separate direct-to-main infrastructure from reviewed data PRs.

## M1 · Structure
- [x] Define stable state, source, and relationship IDs.
- [x] Describe multiple contrasts, mixtures, and contextual directional transitions.
- [x] Implement reference, shape, duplicate, and private-score checks.
- [x] Generate a reproducible manifest and bundled atlas.
- [x] Confirm checks against the foundational draft and empty-main state.

## M2 · Foundation
- [x] Draft foundational, difficult, mixed, and contemplative states.
- [x] Review names and source scope; distinguish editorial synthesis.
- [x] Validate relationships and address independent review findings.
- [x] Open [data PR #2](https://github.com/d4rkd0s/human-emotional-atlas/pull/2) with counts and limitations.
- [ ] Maintainer reviews and merges the data PR.

## M3 · Expansion
- [ ] Track gaps across social emotions, bodily/mental influences, time courses, and traditions.
- [ ] Expand in reviewable batches, normally 10–20 entries where practical.
- [ ] Resolve proposals through source checking, revision, classification, or explicit deferral.
- [ ] Revisit uncertain names and relationships as stronger evidence becomes available.

No milestone asserts exhaustive coverage of every possible human state. Expansion is continuing work.

## M4 · Explorer
- [x] Search/filter states and inspect full descriptions and sources.
- [x] Navigate relationships visually with an accessible list alternative.
- [x] Provide visible copy-paste AI instructions and dataset download.
- [ ] Check mobile layout, keyboard paths, empty state, and load failures.

## M5 · Release
- [x] Infrastructure committed to main; GitHub Validate atlas workflow passed.
- [ ] Enable GitHub Pages and verify successful publication.
- [x] Keep unmerged data out of main and its deployment build.
- [ ] Merge foundation only after maintainer review; verify populated release.

## Coverage backlog

After the foundation, prioritize evidence depth before a raw entry count: richer source-to-claim mapping, cultural comparisons, neurodivergent experiences, social and relational contexts, chronic versus momentary experiences, additional named mixtures, and contradictory transition conditions. Future languages remain possible, but English is the current scope.

## Tracking and verification

Tracking issue: [#1](https://github.com/d4rkd0s/human-emotional-atlas/issues/1). Local checks: 10 integrity/build tests pass; foundational draft validates with 49 states, 109 relationships, and 16 sources. These counts describe proposed data, not reviewed content on main. Desktop and 390px narrow-frame preview checked; search and prompt copying verified.

Pages deployment needs the repository owner to select GitHub Actions in Settings → Pages. The connected tooling cannot change that setting, and the browser is not signed in.

Initial data limitation: intensity and time-course fields currently state general variability rather than entry-specific evidence. Enrich these fields in future reviewed batches. Loneliness, relief, and hatred identify source-fit limits explicitly. The anxiety/fear empirical edge describes semantic proximity, not temporal causation.

## Release checkpoint · 2026-11-06

- Infrastructure commit: `b0ce60e0e47b939557232fcc9383c843a395080d`.
- GitHub validation passed: https://github.com/d4rkd0s/human-emotional-atlas/actions/runs/42334257301
- Proposed data: [d4rkd0s/human-emotional-atlas #2 — Review foundational atlas](https://github.com/d4rkd0s/human-emotional-atlas/pull/2), intentionally unmerged.
- Pages build and tests passed; deployment stopped at configure-pages because Pages is not enabled. Select Settings → Pages → GitHub Actions, then rerun Publish atlas explorer. No administrative credentials are committed.
- Browser checks completed: desktop/narrow-frame render, populated and empty states, search, prompt copy. Full keyboard navigation and simulated network-failure checks remain pending.
