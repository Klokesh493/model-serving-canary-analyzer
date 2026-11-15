# Skills and verification

## What this repository demonstrates

Canary promotion gates, validation of latency and rates, and stable JSON decision reasons.

## Reproduce the result

Run `make verify` and `python3 canary_analyzer.py sample_canaries.csv --json`. Healthy, rollback and hold cases retain their decisions. NaN, infinities, out-of-range rates and invalid traffic percentages hold. Reproduce the primary fixture with `python3 canary_analyzer.py sample_canaries.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The analyzer evaluates exported measurements. Its decision is advisory.

[canary_analyzer.py](../canary_analyzer.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
