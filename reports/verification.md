# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 canary_analyzer.py sample_canaries.csv
ranker-v18: promote
vision-v7: rollback
fraud-v12: hold
test_promotes_healthy_canary (test_canary_analyzer.CanaryAnalyzerTest) ... ok
test_rolls_back_high_error_rate (test_canary_analyzer.CanaryAnalyzerTest) ... ok
test_cli_explains_promote_rollback_and_hold (test_decision_evidence.DecisionEvidenceTest) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.051s

OK
````
