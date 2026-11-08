# Data model

HEA stores UTF-8 JSON as three linked arrays. IDs are stable lowercase slugs; display names may evolve. English is the first release language. Missing knowledge should be described honestly rather than replaced by a fabricated number.

## States

`data/states.json` records `id`, `name`, `kind`, `definition`, `aliases`, `components`, `qualities`, `body`, `thoughts`, `action_tendencies`, `needs`, `contexts`, `examples`, `source_ids`, and `notes`. The optional `basis` identifies the description's evidence context.

Kinds distinguish `emotion`, `mood`, `quality`, `mixed_state`, and `mental_state`. This is an editorial organization, not a universally accepted ontology.

Qualities describe valence, arousal, intensity, and time course in words. Body cues, thoughts, needs, and action tendencies are possibilities, not diagnostic tests. Examples are synthetic illustrations with multiple possible interpretations. Components reference other state IDs and do not assert that a mixture always arises from those components.

## Relationships

`data/relations.json` records `id`, `from`, `to`, `type`, `description`, `conditions`, `counterexamples`, `source_ids`, and `basis`.

| Type | Meaning |
| --- | --- |
| `neighbor` | Related experience or meaningful conceptual proximity |
| `contrast` | A stated dimension of difference, not necessarily a cure |
| `may_transition_to` | A possible directional change under stated conditions |
| `may_cooccur` | States can be present together |
| `component_of` | A state participates in a described mixture |

Transitions and component relations are directional. Neighbor, contrast, and co-occurrence are interpreted symmetrically; store one edge, not redundant reverse edges. The explorer may navigate either endpoint. Contrasts must name or explain their dimension. No opposite is required for every state, and absence of an edge means unmapped, not impossible.

`basis` is `empirical`, `tradition_specific`, or `editorial_synthesis`. It describes the basis of a claim, not a score or universal ranking of traditions. An empirical designation requires a source that supports the specific relationship; an illustrative application of a general theory is editorial synthesis.

## Sources and provenance

`data/sources.json` records `id`, `title`, `url`, `tradition`, `scope`, and `limitations`. State-level references are conceptual anchors, not proof of every listed cue. Relation-level references should be checked against the specific description. Traditional training accounts and phenomenological descriptions retain their framework.

Builder confidence and statistical quality-control notes are excluded from the dataset. Public notes preserve uncertainty and scope. A CC0 dedication covers original HEA text and structure; it does not relicense referenced works.

## Generated files

The build emits `dist/data/manifest.json` with version, counts, and file locations, and `dist/data/atlas.json` with manifest, states, relationships, and sources together. Generated files are not the canonical editing surface. Keep canonical changes in `data/` and follow the current contribution workflow in AGENTS.md.
