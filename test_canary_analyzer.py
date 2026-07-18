import unittest

from canary_analyzer import analyze, canary_decision


class CanaryAnalyzerTest(unittest.TestCase):
    def test_rolls_back_high_error_rate(self):
        row = {"p95_latency_ms": "140", "error_rate": "0.02", "drift_score": "0.01"}
        self.assertEqual(canary_decision(row), "rollback")

    def test_promotes_healthy_canary(self):
        rows = [{"model": "m", "traffic_percent": "5", "p95_latency_ms": "120", "error_rate": "0.001", "drift_score": "0.01"}]
        self.assertEqual(analyze(rows)[0]["decision"], "promote")


if __name__ == "__main__":
    unittest.main()
