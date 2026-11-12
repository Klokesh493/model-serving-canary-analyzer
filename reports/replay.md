# Replay evidence

Captured stdout is compared with a checked-in baseline.

## Demo 1

Result: **PASS**

````text
ranker-v18: promote
vision-v7: rollback
fraud-v12: hold
````

## Decision reasons

Result: **PASS**

````text
[
  {
    "model": "ranker-v18",
    "traffic_percent": 5,
    "decision": "promote",
    "reasons": []
  },
  {
    "model": "vision-v7",
    "traffic_percent": 10,
    "decision": "rollback",
    "reasons": [
      "error_rate_above_1_percent",
      "drift_above_0_10"
    ]
  },
  {
    "model": "fraud-v12",
    "traffic_percent": 3,
    "decision": "hold",
    "reasons": [
      "drift_above_0_07"
    ]
  }
]
````
