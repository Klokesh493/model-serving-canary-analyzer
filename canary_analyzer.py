import argparse
import csv
import json
import math


def assess(row):
    latency = float(row["p95_latency_ms"])
    error_rate = float(row["error_rate"])
    drift = float(row["drift_score"])
    if (not all(math.isfinite(value) for value in (latency, error_rate, drift))
            or latency < 0 or not 0 <= error_rate <= 1 or not 0 <= drift <= 1):
        return "hold", ["invalid_canary_metrics"]
    if "traffic_percent" in row and not 0 <= int(row["traffic_percent"]) <= 100:
        return "hold", ["invalid_traffic_percent"]
    rollback_reasons = [
        name for name, exceeded in (
            ("error_rate_above_1_percent", error_rate > 0.01),
            ("drift_above_0_10", drift > 0.10),
        ) if exceeded
    ]
    if rollback_reasons:
        return "rollback", rollback_reasons
    hold_reasons = [
        name for name, exceeded in (
            ("p95_above_250_ms", latency > 250),
            ("drift_above_0_07", drift > 0.07),
        ) if exceeded
    ]
    if hold_reasons:
        return "hold", hold_reasons
    return "promote", []


def canary_decision(row):
    return assess(row)[0]

def analyze(rows):
    return [{"model": row["model"], "traffic_percent": int(row["traffic_percent"]), "decision": canary_decision(row)} for row in rows]


def main(path, include_evidence=False):
    with open(path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if include_evidence:
        result = []
        for row in rows:
            decision, reasons = assess(row)
            result.append({
                "model": row["model"],
                "traffic_percent": int(row["traffic_percent"]),
                "decision": decision,
                "reasons": reasons,
            })
        print(json.dumps(result, indent=2))
    else:
        for item in analyze(rows):
            print(f'{item["model"]}: {item["decision"]}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate model-serving canaries.")
    parser.add_argument("path")
    parser.add_argument("--json", action="store_true", help="include decision reasons")
    args = parser.parse_args()
    try:
        main(args.path, args.json)
    except (OSError, ValueError, TypeError, KeyError, csv.Error) as error:
        parser.error(str(error))
