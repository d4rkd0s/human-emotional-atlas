# HEA · Human Emotional Atlas

**A public, connected reference dataset for understanding human emotional experience.**

HEA helps agents, AI, and SI explore possible emotional states behind human language and context. It maps emotions, qualities, mixed states, neighbors, contrasts, coexistence, and possible transitions. The consuming system makes its own determinations. HEA is a dataset, not an emotional classifier or a behavioral policy.

[Milestones](MILESTONES.md) · [Data model](docs/DATA_MODEL.md) · [Build directives](AGENTS.md) · [Contributing](CONTRIBUTING.md) · [CC0 license](LICENSE)

## Current status

The infrastructure, validator, build, and explorer are implemented. Ten integrity/build tests pass locally. The first emotional-data load is delivered separately for maintainer review; infrastructure on `main` can run with an empty dataset. An empty explorer means no data has been merged yet, not that data failed to load. See [MILESTONES.md](MILESTONES.md) for completion criteria and release status.

The intended Pages address is **https://d4rkd0s.github.io/human-emotional-atlas/**. It is usable only after Pages deployment succeeds. Until then, use the repository files or build locally.

## Use with an AI

Copy this prompt into an agent with repository or web access:

```text
Use Human Emotional Atlas (HEA) as a descriptive reference dataset:
https://github.com/d4rkd0s/human-emotional-atlas

Read README.md and docs/DATA_MODEL.md, then load data/states.json,
data/relations.json, and data/sources.json from the same commit or branch.
If GitHub Pages is available, data/manifest.json lists the published files
and data/atlas.json bundles the complete published dataset.

The data describes possible states and contextual relationships. It does
not determine a person's emotions or prescribe your behavior. Use its
definitions, alternatives, conditions, counterexamples, and source context
as reference material for your own analysis. Record the revision used.
If the dataset is empty or inaccessible, say so rather than inventing entries.
```

Agents without browsing can use downloaded JSON files. A repository URL alone does not grant an AI access to its contents. For reproducible work, pin a Git commit rather than relying on the moving `main` branch. PR data is provisional until merged by the maintainer.

## What the atlas contains

| Layer | Coverage |
| --- | --- |
| States | Emotions, moods, emotional qualities, mental states, and mixtures |
| Qualities | Valence, arousal, intensity, and time course |
| Experience | Possible bodily sensations, thoughts, action tendencies, and needs |
| Context | Social circumstances and physical or mental influences |
| Language | Synthetic phrases with alternative possible interpretations |
| Relationships | Neighbors, contrasts, co-occurrence, components, and directional transitions |
| Provenance | Source context, limitations, and distinction between research, tradition, and synthesis |

The ambition is broad coverage, not a claim that every human emotion has been enumerated. Multiple contrasts may exist for one state. An opposite is not necessarily an antidote; grief, anger, or fear may be appropriate to circumstances. Mixtures describe experiences, not fixed equations.

## Sources and quality

HEA draws from psychological research, phenomenology, cultural knowledge, and contemplative traditions including Buddhadharma. It aims to express common patterns while preserving meaningful variation. It does not collapse different traditions into one supposedly universal theory or claim to know someone's true inner state from a prompt.

Entries use original descriptions and traceable references. `empirical`, `tradition_specific`, and `editorial_synthesis` identify the basis of relationships. A conceptual source is not proof of every illustrative phrase or bodily cue. Qualifications and counterexamples remain part of the public data.

Builder confidence assessments and statistical quality-control notes stay outside the published dataset. They guide additional verification; they do not establish accuracy. Proposed content is checked, revised, classified in context, or deferred, then reviewed by the maintainer. The purpose is understanding and fair, playful support.

## Repository layout

```text
data/                  Canonical JSON, added and changed through data PRs
schema/                Machine-readable structural contract
scripts/               Dependency-free validation and static build
tests/                 Integrity and build checks
web/                   Searchable atlas and relationship explorer
docs/DATA_MODEL.md     Field and relationship semantics
AGENTS.md              Canonical directives for building HEA
CLAUDE.md              Pointer to the same directives
MILESTONES.md          Progress, evidence, and remaining work
```

The build produces `dist/data/manifest.json`, `dist/data/atlas.json`, individual JSON files, and the explorer. Generated `dist/` is not committed. Colors organize the interface aesthetically and carry no scientific meaning.

## Build and explore locally

Requires Python 3.10+; no Python packages or frontend build dependencies.

```sh
git clone https://github.com/d4rkd0s/human-emotional-atlas.git
cd human-emotional-atlas
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
python3 scripts/build.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000. Serve over HTTP because browsers restrict JSON loading from `file://` pages. To inspect proposed data locally, check out its PR branch before building.

## Review and publishing

- Emotional data and source catalogs: PR, human review by **@d4rkd0s**, then merge.
- Infrastructure, documentation, schema, and website code: direct-to-main changes are allowed for authorized work.
- Automated checks validate references, structure, duplicates, and build integrity. They do not prove psychological truth.
- GitHub Pages publishes `main`, so unmerged PR data is not part of the public explorer.

For first-time hosting, select **Settings → Pages → Source → GitHub Actions**, then run **Publish atlas explorer** or push an infrastructure change. The workflow requires Pages to be enabled; it contains no administrative token. CODEOWNERS requests data review but does not itself enforce branch protection.

## License

Original HEA contributions are dedicated to the public domain under **CC0-1.0**, including commercial reuse. Referenced works retain their own copyrights and terms. Citation does not relicense third-party material.
