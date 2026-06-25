---
id: OPP-YYYYMMDD-slug
title: ""
status: draft
decision: null
score: null
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: ""
tags: []
prompt_versions:
  discovery: v1
  validation: v1
  scoring: v1
  vision: v1
  mvp: v1
  roadmap: v1
  architecture: v1
  success_contract: v1
  portfolio_manager: v1
---

# {Title}

## Discovery

<!-- Paste output from prompts/discovery.md -->

### Problem Statement

Describe the problem in one paragraph. Who has it? How painful is it?

### Market Signal

What evidence suggests this problem matters now?

> **Evidence**: [source, date, metric]

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| | | | |

### Initial Hypothesis

We believe [target user] will [behavior] because [reason].

### Open Questions

- [ ] Question 1
- [ ] Question 2

---

## Validation

<!-- Paste output from prompts/validation.md -->

### Experiments

| # | Experiment | Hypothesis | Method | Success Criteria | Status |
|---|------------|------------|--------|------------------|--------|
| 1 | | | | | planned |

### Results

Summarize experiment outcomes with evidence.

> **Evidence**: [source, date, metric]

### Kill / Continue Signals

- **Continue if**: ...
- **Kill if**: ...

---

## Scoring

<!-- Paste output from prompts/scoring.md. See playbooks/scoring-rules.md -->

| Dimension | Raw (0–10) | Weight | Weighted | Rationale |
|-----------|------------|--------|----------|-----------|
| Problem severity | | 20% | | |
| Market size and timing | | 15% | | |
| Validation strength | | 25% | | |
| Competitive moat | | 15% | | |
| Execution feasibility | | 15% | | |
| Strategic fit | | 10% | | |
| **Total** | | **100%** | **XX** | |

**Final score**: XX

**Decision mapping**: BUILD (>= 70) | MONITOR (40–69) | KILL (< 40)

---

## Product Vision

<!-- Paste output from prompts/vision.md -->

### Target User

Who is the primary user? Be specific (role, company size, context).

### Value Proposition

One sentence: We help [user] do [outcome] by [approach].

### Differentiation

What makes this different from alternatives?

### North Star Metric

The single metric that best captures value delivered.

---

## MVP Definition

<!-- Paste output from prompts/mvp.md -->

### Scope In

- Item 1
- Item 2

### Scope Out

- Item 1
- Item 2

### Success Metrics

| Metric | Target | Measurement method |
|--------|--------|--------------------|
| | | |

### Smallest Testable Slice

The minimum build or experiment to validate core value.

---

## Roadmap

<!-- Paste output from prompts/roadmap.md -->

### Phase 1: {Name} (Weeks X–Y)

- Milestone 1
- Milestone 2

**Dependencies**: ...

### Phase 2: {Name} (Weeks X–Y)

- Milestone 1

### Resource Assumptions

| Role | Allocation | Duration |
|------|------------|----------|
| | | |

---

## Architecture Proposal

<!-- Paste output from prompts/architecture.md. Documentation only — no code -->

### System Overview

High-level description of components and data flow.

### Build vs Buy

| Component | Decision | Rationale |
|-----------|----------|-----------|
| | build / buy | |

### Integration Points

External systems, APIs, or data sources required.

### Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| | | | |

---

## Success Contract

<!-- Paste output from prompts/success-contract.md -->

### Commitments

| Commitment | Metric | Target | Review Date |
|------------|--------|--------|-------------|
| | | | |

### Review Schedule

- First review: YYYY-MM-DD
- Cadence: every 30 days (BUILD) / 90 days (MONITOR)

### Exit Triggers

Conditions that trigger re-evaluation or kill:

- Trigger 1: ...
- Trigger 2: ...

---

## Final Decision

<!-- Paste output from prompts/portfolio-manager.md -->

| Field | Value |
|-------|-------|
| **Decision** | build / monitor / kill |
| **Score** | XX |
| **Date** | YYYY-MM-DD |
| **Rationale** | |

### Next Actions

- [ ] Action 1
- [ ] Action 2

### Dissent (if any)

Record any disagreement and reasoning.

### Portfolio Update

- [ ] Added to [portfolio/active.md](../portfolio/active.md) / [monitoring.md](../portfolio/monitoring.md) / [archived.md](../portfolio/archived.md)
