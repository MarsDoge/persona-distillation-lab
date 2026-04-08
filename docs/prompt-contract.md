# Prompt Contract v1

## Purpose
This contract defines how persona invocation should be expressed.
It exists so routing and panel composition can be tested more consistently.

## Required fields
- task
- selected_persona_mode (`single`, `dual`, `panel`)
- selected_personas
- expected_output_shape

## Optional fields
- conflict_axis
- synthesis_required
- benchmark_context

## Contract rule
A persona invocation should state why the selected mode fits the task shape.
It should not select personas arbitrarily.
