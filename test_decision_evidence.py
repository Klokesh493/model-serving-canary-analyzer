import json
import subprocess
import sys
import unittest


class DecisionEvidenceTest(unittest.TestCase):
    def test_cli_explains_promote_rollback_and_hold(self):
        command = [sys.executable, "canary_analyzer.py", "sample_canaries.csv"]
        self.assertEqual(subprocess.check_output(command, text=True).splitlines(),
                         ["ranker-v18: promote", "vision-v7: rollback", "fraud-v12: hold"])
        results = json.loads(subprocess.check_output(command + ["--json"], text=True))
        self.assertEqual([item["decision"] for item in results], ["promote", "rollback", "hold"])
        self.assertEqual([item["reasons"] for item in results], [
            [], ["error_rate_above_1_percent", "drift_above_0_10"], ["drift_above_0_07"]
        ])
