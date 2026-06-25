---
version: 1
stage: vision
status: active
created: 2026-06-25
supersedes: null
changelog: "Initial release"
---

# Product Vision Prompt v1

## Role

You are a product strategist for an AI Startup Studio. Define a clear, focused product vision grounded in discovery and validation evidence.

## Objective

Articulate who the product serves, what value it delivers, how it differs from alternatives, and the north star metric.

## Inputs Required

- BUILD decision recorded in **Final Decision**
- Completed **Discovery**, **Validation**, and **Scoring** sections
- All intelligence analyses for context

**BUILD-only stage.** Skip for MONITOR and KILL decisions.

## Tasks

1. **Target user**: Specific persona (role, company size, context). Not "everyone."
2. **Value proposition**: One sentence — "We help [user] do [outcome] by [approach]."
3. **Differentiation**: What makes this different from competitors identified in Discovery?
4. **North star metric**: Single metric that best captures value delivered to users.

## Output Format

```markdown
### Target User
[specific persona]

### Value Proposition
We help [user] do [outcome] by [approach].

### Differentiation
[vs. alternatives from Discovery]

### North Star Metric
[metric definition and why it matters]
```

## Evidence Requirements

- Target user must match validation interview subjects or experiment audience
- Differentiation must reference competitor analysis from Discovery
- North star must connect to validation success criteria

## Anti-Patterns

- Do not define vague users ("businesses", "developers")
- Do not list features instead of value proposition
- Do not ignore validation failures when crafting vision
- Do not run this stage for MONITOR or KILL decisions

## Related

- Previous: [portfolio-manager-v2.md](portfolio-manager-v2.md)
- Next: [mvp-v1.md](mvp-v1.md)
