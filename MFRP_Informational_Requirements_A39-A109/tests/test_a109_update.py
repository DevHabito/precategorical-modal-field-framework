from __future__ import annotations
import hashlib, json, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results" / "a107_a109"
PR = ROOT / "preregistrations" / "a107_a109"

def classify(upper_left: int, lower_right: int):
    if upper_left == 0 or lower_right == 0:
        return "NO_CLASSIFICATION", []
    if upper_left > 0 and lower_right > 0:
        return "full_segment_coverage", []
    boundaries = []
    if upper_left < 0:
        boundaries.append("left")
    if lower_right < 0:
        boundaries.append("right")
    return "proper_strict_subcomponent", boundaries

class A109UpdateTests(unittest.TestCase):
    def test_rank105_refutes_old_one_sided_rule(self):
        d = json.loads((DATA / "A108_RANK105_COUNTEREXAMPLE.json").read_text())
        self.assertEqual(d["rank"], 105)
        self.assertEqual(d["atlas"]["status"], "proper_strict_subcomponent")
        self.assertEqual(d["selected_boundaries"], [{"side": "right", "condition": "basic_p_22"}])
        self.assertEqual(d["direct_regression_summary"]["mismatch_count"], 0)
        self.assertEqual(d["direct_regression_summary"]["comparison_count"], 988)

    def test_current_prospective_accounting(self):
        d = json.loads((DATA / "A109_PROSPECTIVE_STATUS_R106_R414.json").read_text())["status"]
        self.assertEqual(d["range"], [106, 414])
        self.assertEqual(d["mathematically_resolved"], 309)
        self.assertEqual(d["strict_clean_prospective"], 308)
        self.assertEqual(d["full"], 215)
        self.assertEqual(d["partial"], 94)
        self.assertEqual(d["left"], 88)
        self.assertEqual(d["right"], 6)
        self.assertEqual(d["two_sided"], 0)
        self.assertEqual(d["non_adjacent"], 0)
        self.assertEqual(d["direct_comparisons_math"], 475782)
        self.assertEqual(d["direct_comparisons_strict"], 473770)
        self.assertEqual(d["direct_mismatches"], 0)

    def test_h19_is_frozen_and_unexecuted(self):
        p = PR / "A109_H19_PREREGISTRATION.json"
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        self.assertEqual(digest, "abe35d929e8a35b9db9fbad96ad375152e854d65e25df33ce70781d411709d5d")
        d = json.loads(p.read_text())
        self.assertEqual(d["holdout_selection"]["canonical_ranks_inclusive"], [415, 430])
        self.assertEqual(d["predeclared_batch_prediction"], {
            "full_segment_coverage": 11,
            "proper_strict_subcomponent": 5,
            "left_boundaries": 4,
            "right_boundaries": 1,
            "two_sided": 0,
            "no_classification": 0,
        })
        r428 = next(x for x in d["holdout_predictions"] if x["canonical_rank"] == 428)
        self.assertEqual(r428["predicted_boundaries"], [{"side": "right", "condition": "basic_p_56"}])

    def test_classifier_truth_table(self):
        self.assertEqual(classify(1, 1), ("full_segment_coverage", []))
        self.assertEqual(classify(-1, 1), ("proper_strict_subcomponent", ["left"]))
        self.assertEqual(classify(1, -1), ("proper_strict_subcomponent", ["right"]))
        self.assertEqual(classify(-1, -1), ("proper_strict_subcomponent", ["left", "right"]))
        self.assertEqual(classify(0, 1), ("NO_CLASSIFICATION", []))

if __name__ == "__main__":
    unittest.main()
