# Model Serving Canary Analyzer walkthrough

## Business problem

Evaluates model-serving canaries using latency, error rate, and prediction drift before routing more traffic.

## Reproduce the workflow

Run `python3 canary_analyzer.py sample_canaries.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
ranker-v18: promote
vision-v7: rollback
fraud-v12: hold
```

The sample supplies these fields. `model`, `traffic_percent`, `p95_latency_ms`, `error_rate`, `drift_score`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.

## Review the decision evidence

Run `python3 canary_analyzer.py sample_canaries.csv --json`. The vision model
triggers both rollback reasons. The fraud model only crosses the lower drift
threshold, so its recommendation is hold. The JSON preserves traffic
percentage so the operator can see which stage the evidence came from.
The regression test checks that the original text output stays stable.
