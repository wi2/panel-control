# Prompts

Versioned AI prompts for each stage of the evaluation pipeline.

## Current Versions

| Stage | Index | Active Version |
|-------|-------|----------------|
| Discovery | [discovery.md](discovery.md) | v1 |
| Validation | [validation.md](validation.md) | v1 |
| Scoring | [scoring.md](scoring.md) | v1 |
| Product Vision | [vision.md](vision.md) | v1 |
| MVP Definition | [mvp.md](mvp.md) | v1 |
| Roadmap | [roadmap.md](roadmap.md) | v1 |
| Architecture | [architecture.md](architecture.md) | v1 |
| Success Contract | [success-contract.md](success-contract.md) | v1 |
| Portfolio Manager | [portfolio-manager.md](portfolio-manager.md) | v1 |

## Versioning

- **Canonical content** lives in `{stage}-v{N}.md`.
- **Index file** `{stage}.md` points to the current version and lists changelog.
- Integer versions only: `v1`, `v2`, `v3`, …
- Never delete deprecated prompts; mark `status: deprecated` and set `superseded_by`.

### When to Bump Version

| Change type | Action |
|-------------|--------|
| Typo or clarity fix (no output change) | Edit in place if unused; otherwise bump |
| New questions or criteria | Create v{N+1} |
| Changed output format | Create v{N+1} |
| Changed scoring weights referenced | Create v{N+1} |

### Prompt Frontmatter

```yaml
---
version: 1
stage: discovery
status: active
created: 2026-06-25
supersedes: null
changelog: "Initial release"
---
```

## Usage

1. Open the index file for the stage (e.g. `discovery.md`).
2. Follow the link to the active version (e.g. `discovery-v1.md`).
3. Provide the prompt to your AI assistant with the required inputs.
4. Paste the output into the matching section of the opportunity document.
5. Record the version used in opportunity frontmatter (`prompt_versions`).

## Pipeline Order

```text
discovery → validation → scoring → vision → mvp → roadmap → architecture → success-contract → portfolio-manager
```

See [evaluation process](../playbooks/evaluation-process.md).

## Related

- [Conventions](../CONVENTIONS.md)
- [Contributing](../CONTRIBUTING.md)
