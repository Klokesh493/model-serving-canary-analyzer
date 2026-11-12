# Model Serving Canary Analyzer runbook

## What the project does

A serving rollout needs a documented decision before expanding traffic when error rate, tail latency, and prediction drift disagree.

See the [architecture and data flow](ARCHITECTURE.md) and [project case study](CASE_STUDY.md).

## Run from a clean checkout

Use Python 3 and Make. Install the pinned developer tools in a local environment.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

Run a bundled scenario from the repository root.

```sh
python3 canary_analyzer.py sample_canaries.csv
```

## Expected result

- Demo 1. `3 lines of output. Open the baseline for the full result.` [Baseline](../examples/Demo%201.stdout.txt)
- Decision reasons. `25 lines of output. Open the baseline for the full result.` [Baseline](../examples/Decision%20reasons.stdout.txt)

Run `make replay` to compare results with the baselines and regenerate the [replay report](../reports/replay.md).
The [rules page](RULES.md) links to the code behind the decision.

## Verify a change

Run `make check PYTHON=python` inside the virtual environment. This runs the application checks, Ruff lint, and the Bandit static gate.
The [development guide](DEVELOPMENT.md) explains the tools and the [local report](../reports/devsecops.md) records what passed.

## If a check fails

Run the first failing command on its own. For a replay mismatch, inspect the diff and compare the input, rule, and expected output before updating the baseline.
For a lint or Bandit finding, review the reported source line and rerun the relevant target.

## Golden note

Use JSON output for rollout evidence. Review error and drift rollback reasons before lower-priority hold conditions.

## Operating limits

Use the [case study](CASE_STUDY.md) to check assumptions before applying a result to a live environment.
