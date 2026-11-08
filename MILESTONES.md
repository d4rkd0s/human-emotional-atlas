# HEA milestones

Updated 2026-11-08. This is the canonical progress tracker. The maintainer merged foundation PR #2 and has authorized ongoing work directly on main, without new PRs. Validation and source review still apply.

| Marker | Milestone | Status | Evidence / remaining work |
| --- | --- | --- | --- |
| M0 | Definition and governance | Complete | README, AGENTS, CLAUDE, contribution rules, CC0; current direct-to-main directive recorded |
| M1 | Data contract and build | Complete | Schemas, reference validator, deterministic bundle, 10 integrity/build tests |
| M2 | Foundational dataset | Complete | Maintainer merged PR #2; 49 states and 109 relationships on main |
| M3.1 | First enrichment batch | Complete | 15 states enriched; four targeted primary studies added; 20 total sources |
| M3.2 | Broader coverage and evidence depth | Ongoing | Remaining qualitative fields, source-to-claim detail, cultural variation, additional states |
| M4 | Initial explorer | Complete | Search, filter, state detail, sources, map/list, copy prompt, download; browser smoke checks |
| M5 | Hosted release | Blocked on Pages setting | Code/data available publicly; site build passes; Pages must be enabled by owner |

## M0 · Definition
- [x] Establish descriptive purpose without an inference engine or behavioral policy.
- [x] Capture interview decisions in AGENTS.md, with CLAUDE.md pointing to it.
- [x] Set English-first, CC0, broad source eligibility, and contextual provenance.
- [x] Record the latest maintainer instruction: no new PRs for authorized ongoing work.

## M1 · Structure
- [x] Stable state, source, and relationship IDs.
- [x] Multiple contrasts, mixtures, and contextual directional transitions.
- [x] Reference, shape, duplicate, component-cycle, and private-score checks.
- [x] Reproducible manifest and bundled atlas.
- [x] Validate populated and empty datasets.

## M2 · Foundation
- [x] Foundational, difficult, mixed, and contemplative states.
- [x] Review names, source scope, and evidence classification.
- [x] Address independent review findings.
- [x] Maintainer merged [d4rkd0s/human-emotional-atlas #2 — Review foundational atlas](https://github.com/d4rkd0s/human-emotional-atlas/pull/2).

## M3 · Evidence and coverage
- [x] Identify generic fields and weak source fit in the foundation.
- [x] Enrich intensity/time course for joy, sadness, grief, fear, anxiety, anger, frustration, shame, guilt, relief, loneliness, hatred, envy, compassion, and equanimity.
- [x] Add targeted primary studies for loneliness, relief, and hatred; replace mismatched conceptual anchors.
- [x] Preserve qualitative/editorial labels and study limitations; do not manufacture probabilities.
- [ ] Enrich the remaining 34 states' generic intensity/time-course fields.
- [ ] Improve claim-level provenance for body cues, needs, and proposed transitions.
- [ ] Expand cultural and neurodivergent perspectives without treating any group as uniform.
- [ ] Add additional states and mixtures after naming and source checks.
- [ ] Continue revisiting disputed or weakly supported relationships.

M3 is continuing research, not a promise to enumerate every possible human state. A merged entry is not a claim of scientific certainty.

## M4 · Initial explorer
- [x] Search/filter states and inspect descriptions, examples, and sources.
- [x] Navigate a selected state's relationships visually and through a full list.
- [x] Visible copy-paste AI prompt and generated JSON download.
- [x] Desktop and 390px narrow-frame layout inspected.
- [x] Populated and empty-state rendering checked.
- [x] Keyboard activation of graph nodes and map visibility control checked.
- [x] Mixed-state filter checked.
- [x] Missing-data response checked by temporarily withholding a generated JSON file; error message rendered and data returned after restoration/live reload.

These are bounded smoke checks, not a comprehensive accessibility certification or device matrix. The retry button's isolated click path was not verified because preview live reload restored the page first.

## M5 · Hosted release
- [x] Public repository, CC0 license, merged foundation, documentation, and successful validation workflow.
- [x] Static site builds with populated data.
- [ ] Owner enables Settings → Pages → Source → GitHub Actions.
- [ ] Rerun Publish atlas explorer and verify public deployment.

The connector cannot change Pages settings, and the cloud browser is not signed into the owner's account. This blocks hosting only. Continue data and code work on main.

## Verification and history

Tracking issue: [d4rkd0s/human-emotional-atlas #1 — HEA milestones](https://github.com/d4rkd0s/human-emotional-atlas/issues/1).

- Foundation: 49 states, 109 relationships, originally 16 sources; merged by maintainer on 2026-11-06 (America/Chicago).
- Enrichment 001: same state/relationship counts, 20 sources, 15 enriched entries.
- Ten integrity/build tests and validator pass locally. Foundation GitHub validation passed.
- Pages tests/build passed; configure-pages failed because the site is not enabled.

Earlier references to awaiting PR #2 review or empty main data are superseded by this tracker.
