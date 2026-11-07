# Contributing

HEA is maintained by d4rkd0s with AI-assisted research, drafting, and review. Contributions are welcome under CC0-1.0.

Emotional data and source changes require a pull request and maintainer review. Code and documentation may be pushed directly to main by the maintainer or an authorized collaborator. CODEOWNERS routes reviews; repository protection is a separate GitHub setting.

Keep batches understandable. Prefer 10–20 entries per review when practical; a first coherent foundation may be larger. Explain the coverage, naming decisions, relationships, and gaps in each PR. Do not silently merge data to make the website look populated.

Read AGENTS.md and docs/DATA_MODEL.md before drafting. Consult original sources, preserve cultural context, write original prose, and distinguish direct evidence from editorial synthesis. Source citations are not a license to reproduce third-party text or datasets. Do not submit private messages or identifiable human accounts as examples; write illustrative examples instead.

Name states through comparison: identify established terms, compare scope and ambiguity, pick the clearest English term, preserve useful aliases, and have a second reviewer challenge the choice. Descriptive mixtures are valid when no established name fits. Components describe co-presence, not a universal formula.

Builder confidence assessments remain outside version control. Use them to target verification, not to declare truth. Review can resolve a proposal as accepted, revised, tradition-specific, disputed, or deferred for insufficient support. Public qualifications remain visible.

Run:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
python3 scripts/build.py
```

By contributing, you dedicate your original contribution under CC0-1.0. Cited works retain their own terms.
