# Model Serving Canary Analyzer architecture

Evaluates model-serving canaries using latency, error rate, and prediction drift before routing more traffic.

```mermaid
flowchart LR
    N0["sample_canaries.csv"]
    N1["canary_analyzer.py"]
    N2["canary decision / analyze"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
