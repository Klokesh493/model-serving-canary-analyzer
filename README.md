# Model Serving Canary Analyzer

Evaluates model-serving canaries using latency, error rate, and prediction drift before routing more traffic.

Focus: model serving, canary release, SLOs, MLOps.

Portfolio framing: Apple-scale client-style AI platform project using synthetic data only.

## Run

```bash
python3 canary_analyzer.py sample_canaries.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```
