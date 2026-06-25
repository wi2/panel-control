# Glossary

Terms used throughout the AI Startup Studio control plane.

## A

### Architecture Proposal

High-level system design for an opportunity: components, build-vs-buy choices, integration points, and technical risks. Documentation only—no application code.

## B

### BUILD

Portfolio decision for opportunities scoring **>= 70**. Indicates sufficient evidence and fit to allocate build resources. Recorded in [`portfolio/active.md`](../portfolio/active.md).

## C

### Control Plane

This repository. The central system for evaluating, documenting, and managing startup opportunities—not the products themselves.

## D

### Discovery

First pipeline stage. Identifies the problem, market signals, competitors, and initial hypothesis. Driven by [`prompts/discovery.md`](../prompts/discovery.md).

## E

### Evidence

Documented support for a claim: source, date, and metric. Required for scoring and decisions. Format:

```markdown
> **Evidence**: [source, date, metric]
```

### Evaluation Pipeline

The sequential process: Discovery → Validation → Scoring → Product Vision → MVP Definition → Roadmap → Architecture → Success Contract → Portfolio Management.

## K

### KILL

Portfolio decision for opportunities scoring **< 40**, or meeting automatic kill triggers. Terminates further investment. Recorded in [`portfolio/archived.md`](../portfolio/archived.md).

## M

### MONITOR

Portfolio decision for opportunities scoring **40–69**. Insufficient evidence to build; worth tracking with periodic re-evaluation. Recorded in [`portfolio/monitoring.md`](../portfolio/monitoring.md).

### MVP Definition

Minimum viable product scope: what is in, what is out, success metrics, and the smallest testable slice. Driven by [`prompts/mvp.md`](../prompts/mvp.md).

## O

### Opportunity

A single startup idea under evaluation. One markdown file in [`opportunities/`](../opportunities/) per opportunity, following [`templates/opportunity-template.md`](../templates/opportunity-template.md).

## P

### Portfolio

The set of all evaluated opportunities, split by decision: active (BUILD), monitoring (MONITOR), archived (KILL).

### Prompt Version

A numbered revision of a pipeline-stage prompt (e.g. `discovery-v1`, `discovery-v2`). Opportunities record which versions were used for reproducibility.

## R

### Roadmap

Phased plan for delivering the opportunity: milestones, dependencies, and resource assumptions. Driven by [`prompts/roadmap.md`](../prompts/roadmap.md).

## S

### Scoring

Quantitative evaluation (0–100) across weighted dimensions. Driven by [`prompts/scoring.md`](../prompts/scoring.md) and [`playbooks/scoring-rules.md`](../playbooks/scoring-rules.md).

| Decision | Score |
|----------|-------|
| BUILD | >= 70 |
| MONITOR | 40–69 |
| KILL | < 40 |

### Success Contract

Measurable commitments, review dates, and exit triggers for a BUILD opportunity. Defines what success looks like and when to re-evaluate or kill. Driven by [`prompts/success-contract.md`](../prompts/success-contract.md).

## V

### Validation

Second pipeline stage. Designs and records experiments to test the discovery hypothesis. Driven by [`prompts/validation.md`](../prompts/validation.md).

### Validation Experiment

A time-boxed test designed to produce evidence for or against a hypothesis (e.g. customer interviews, landing page, concierge MVP).

## Related

- [Philosophy](philosophy.md)
- [Principles](principles.md)
- [Conventions](../CONVENTIONS.md)
