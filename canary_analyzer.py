import csv
import sys


def canary_decision(row):
    latency = float(row["p95_latency_ms"])
    error_rate = float(row["error_rate"])
    drift = float(row["drift_score"])
    if error_rate > 0.01 or drift > 0.10:
        return "rollback"
    if latency > 250 or drift > 0.07:
        return "hold"
    return "promote"


def analyze(rows):
    return [{"model": row["model"], "traffic_percent": int(row["traffic_percent"]), "decision": canary_decision(row)} for row in rows]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for item in analyze(csv.DictReader(handle)):
            print(f'{item["model"]}: {item["decision"]}')


if __name__ == "__main__":
    main(sys.argv[1])
