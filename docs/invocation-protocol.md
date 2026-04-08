# Persona Invocation Protocol

## Goal

Use distilled personas as **reasoning constraints**, not as tone skins.

A persona skill should shape:
- what the model pays attention to
- how it frames the problem
- which heuristics it prefers
- which anti-patterns it rejects
- where it should stay uncertain

It should **not** be used as mere roleplay or quote cosplay.

---

## Core contract

When invoking a persona skill, the agent must:

1. read the target persona skill first
2. apply its mental models and decision heuristics to the task
3. respect its anti-patterns and honest limits
4. keep task reality and evidence above style mimicry
5. avoid pretending to literally be the historical person

### Correct mental model

```text
Task
→ load persona skill
→ use persona cognition as reasoning constraint
→ produce task output
```

### Wrong mental model

```text
Task
→ imitate tone / quotes / surface mannerisms
→ produce theatrical answer
```

---

## Invocation structure

A correct invocation should include these layers:

### 1. Persona loading
Example:

```text
Read `personas/elon-musk/SKILL.md` first.
```

### 2. Constraint framing
Example:

```text
Use this skill as a cognitive operating system, not as roleplay.
Prioritize its mental models, decision heuristics, anti-patterns, and honest limits.
```

### 3. Task execution
Example:

```text
Analyze whether this AI infra product should optimize for speed, cost, or defensibility first.
```

### 4. Output discipline
Example:

```text
Do not only mimic tone. Show the reasoning structure.
If evidence is insufficient, preserve uncertainty.
```

---

## Engine-specific examples

### OpenClaw

```text
Use `personas/elon-musk/SKILL.md` as the reasoning constraint layer.
Do not use it only for tone. Use its mental models and anti-patterns to evaluate this strategy question.
```

### Claude Code

```bash
claude --print "Read personas/elon-musk/SKILL.md first. Use it as a cognitive operating system, not as roleplay. Analyze this architecture decision with its mental models, heuristics, anti-patterns, and honest limits."
```

### Codex

```bash
codex exec "Read personas/elon-musk/SKILL.md. Use it as a reasoning constraint, not a tone overlay. Then propose a product/engineering decision and explain the tradeoff structure."
```

---

## Guardrails

### Required
- reasoning > tone
- evidence > theatrics
- distinction > generic smart-sounding output
- uncertainty when the persona would lack enough information

### Forbidden
- quote imitation as the main value
- pretending the model has direct access to the real person
- dropping honest limits
- using persona skin to override task evidence

---

## Output expectation

A good persona-invoked answer should make a reader feel:
- this problem was framed differently
- different tradeoffs were highlighted
- different failure modes were rejected
- the reasoning is recognizably persona-specific

Not merely:
- the wording sounds like the person

---

## Design rule for future personas

Every persona skill in this lab should be written so it can be used by:
- OpenClaw
- Claude Code
- Codex
- future agent runtimes

Therefore each persona should expose:
- expression DNA
- core mental models
- decision heuristics
- anti-patterns / refusal patterns
- suitable / unsuitable use cases
- honest limits

This makes the persona a reusable cognitive adapter layer.
