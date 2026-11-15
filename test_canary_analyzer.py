import unittest

from canary_analyzer import analyze, assess, canary_decision


class CanaryAnalyzerTest(unittest.TestCase):
    def test_rolls_back_high_error_rate(self):
        row = {"p95_latency_ms": "140", "error_rate": "0.02", "drift_score": "0.01"}
        self.assertEqual(canary_decision(row), "rollback")

    def test_promotes_healthy_canary(self):
        rows = [{"model": "m", "traffic_percent": "5", "p95_latency_ms": "120", "error_rate": "0.001", "drift_score": "0.01"}]
        self.assertEqual(analyze(rows)[0]["decision"], "promote")

    def test_invalid_telemetry_holds_promotion(self):
        healthy = {"p95_latency_ms": "120", "error_rate": "0.001", "drift_score": "0.01"}
        for field, value in (
            ("error_rate", "NaN"), ("p95_latency_ms", "-1"), ("drift_score", "inf"),
            ("error_rate", "1.1"),
        ):
            with self.subTest(field=field, value=value):
                self.assertEqual(assess({**healthy, field: value}), ("hold", ["invalid_canary_metrics"]))
        self.assertEqual(assess({**healthy, "traffic_percent": "101"}), ("hold", ["invalid_traffic_percent"]))


if __name__ == "__main__":
    unittest.main()
