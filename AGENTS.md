# Building HEA

HEA is a descriptive reference dataset, not an inference service or a behavioral policy for consuming agents. Preserve the maintainer's scope in README.md.

## Maintainer vision and interview decisions
- Name: HEA, Human Emotional Atlas. Canonical repository: d4rkd0s/human-emotional-atlas.
- Purpose: improve agents', AI's, and SI's understanding of possible underlying human emotional states in prompts, language, and context. Consumers make their own determinations; do not prescribe their response style or hide an analysis engine in the site.
- Aim for broad, dense coverage of emotions and emotional qualities, including difficult states, mixed states, neighboring emotions, multiple kinds of opposites, coexistence, and transitions. More relevant information is welcome; unsupported filler is not.
- Include intensity, valence, arousal, duration, bodily sensations, thoughts, action tendencies, needs, social context, physical and mental influences, alternative interpretations, and feedback in both directions.
- Describe transitions associated with events, responses, and spontaneous change, including intensification. Contrast is not automatically an antidote. Helpful conditions are contextual descriptions, not manipulation recipes or guaranteed cures.
- The purpose is understanding and fair, playful help. No goal of covertly changing or manipulating people. Allow emotions to remain appropriate to their situation.
- Seek common human patterns without imposing one school's opinions or erasing cultural, individual, and contextual variation. There is no verified universal median or exhaustive inventory.
- All source traditions are eligible, including dense emotional wisdom in Buddhadharma. Distinguish framework-specific accounts from empirical research. No claim to certainty about a person's inner state.
- Use agentic comparison and independent review to choose the best supported, clear name for each state. Mixed emotions can form distinct states; map both named mixtures and descriptive combinations.
- English only initially. Use stable identifiers so future translations can be added. No translation infrastructure is required now.
- Public Git repository, CC0-1.0, simple to use with AI, plus a sleek GitHub Pages website with search, a relationship map, and a visible copy-paste data-access prompt.
- Use a red/orange/yellow/green/blue/indigo/violet palette as aesthetic inspiration only. Do not mention chakras in the product UI or imply colors are scientific measurements.
- Keep it simple: no runtime API, account system, paid service, or unnecessary dependencies. Build in milestones and track them in the repository.
- Current maintainer directive (2026-11-08): keep authorized ongoing work on main with no new PRs. This supersedes the earlier mandatory data-PR workflow; preserve validation, source checking, and transparent change summaries.

## Change boundaries
- Code, schema, documentation, and website infrastructure may go directly to main.
- Maintainer-authorized data and source changes may go directly to main after checks. Do not create PRs for the current work. External contributions still use PRs; no blanket authorization to merge unrelated outside contributions.
- Use focused parallel agents for research, drafting, and independent review. Assign disjoint files; integrate through one owner.
- Update MILESTONES.md when evidence supports a status change. Do not mark research complete merely because files exist.

## Research and drafting
- Consult primary scientific work, lived-experience literature, cultural sources, and contemplative traditions including Buddhadharma. No tradition is excluded by default.
- Preserve each source's framework, population, scope, and limitations. Tradition-specific claims do not become universal empirical findings.
- Write original summaries. CC0 applies to HEA contributions, not cited third-party works.
- Prefer established English names; use a clear descriptive name when no established name fits. Record aliases and explain mixtures without presenting them as chemical equations.
- Cite conceptual anchors honestly. Mark editorial synthesis as such; a nearby source does not prove every bodily cue or transition.
- Assess confidence during building and challenge it through independent source checking. Keep numerical confidence, statistical review notes, and provisional scoring outside tracked/public files. Do not manufacture probabilities.
- Uncertainty, context, alternative interpretations, and counterexamples belong in the public descriptions.
- No exhaustive-completeness claim, universal emotional diagnosis, or deterministic antidote claim.

## Validation
Run `python3 -m unittest discover -s tests -v`, `python3 scripts/validate.py`, and `python3 scripts/build.py` before delivery. Verify affected website behavior and small-screen layout. Data change summaries must include counts, sources, naming decisions, and unresolved limits, whether delivered as commits or external PRs.
