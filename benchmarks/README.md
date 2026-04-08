# Persona Benchmarks

This module evaluates whether a distilled persona is:
- distinct
- stable
- useful
- bounded by honest limits

It also tracks where a persona is strong or weak through a radar-style scoring system.

## Structure

- `turing-test/` question sets grouped by domain
- `scoring/` shared dimensions, rubric, and templates
- `results/` persona-specific benchmark outputs

## Purpose

The benchmark system is not trying to find a universal best persona.
It is trying to make each persona legible:
- what it is good at
- what it is weak at
- where it should be routed
- where it should not be trusted too much
