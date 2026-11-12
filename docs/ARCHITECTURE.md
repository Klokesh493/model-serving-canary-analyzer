# Model Serving Canary Analyzer architecture

Evaluates model-serving canaries using latency, error rate, and prediction drift before routing more traffic.

```mermaid
flowchart LR
    A["Canary latency, error rate, and drift"]
    B["Apply error and drift rollback thresholds"]
    C{"Rollback threshold crossed?"}
    D["Rollback"]
    E["Otherwise hold on latency or moderate drift, else promote"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
