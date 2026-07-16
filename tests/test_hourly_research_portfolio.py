from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO = ROOT / "steward" / "research-portfolio.json"


class HourlyResearchPortfolioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(PORTFOLIO.read_text(encoding="utf-8"))

    def test_active_lane_and_ready_work_exist(self) -> None:
        active = [lane for lane in self.data["lanes"] if lane["state"] == "ACTIVE"]
        self.assertEqual([lane["id"] for lane in active], [self.data["north_star_lane"]])
        ready = [
            item
            for item in active[0]["internal_work_items"]
            if item["state"] == "READY" and item["hourly_eligible"]
        ]
        self.assertGreaterEqual(len(ready), 1)
        # Explicit rank overrides raw priority_score. The real physical witness
        # led and EXECUTED its REACH swing on 2026-07-16
        # (explorations/2026-07-16-real-physical-witness/); per the lane-doctrine
        # invariant (a leading item resolved -> continue pushing the core through
        # its typed interface), priority reverted to P2C-BOUNDARY-ADAPTER, which
        # then executed the witness-consuming QIP adapter. That exposed the
        # target-phase whole-family admission residual, so priority now moves to
        # P2C-NULL-COMPLETION-CLOSURE (rerank_2026_07_16c).
        self.assertTrue(self.data["selection_contract"][
            "explicit_rank_field_overrides_priority_score"])
        selected = min(ready, key=lambda item: item["rank"])
        self.assertEqual(selected["id"], "P2C-NULL-COMPLETION-CLOSURE")

    def test_hard_core_and_doctrine_fields(self) -> None:
        self.assertIn("HARD-CORE.md", self.data["hard_core"]["statement_owner"])
        self.assertIn("reach swing", self.data["selection_contract"]["reach_swing_cadence"])
        for lane in self.data["lanes"]:
            self.assertTrue(lane.get("relation_to_hard_core"))
            for item in lane.get("internal_work_items", []):
                self.assertTrue(item.get("relation_to_hard_core"))

    def test_gated_work_has_activation_and_material_rule(self) -> None:
        for lane in self.data["lanes"]:
            for item in lane.get("internal_work_items", []):
                if item["state"].startswith("GATED"):
                    self.assertTrue(item.get("activation"))
        contract = self.data["selection_contract"]
        self.assertTrue(contract["select_highest_ranked_unblocked_item"])
        self.assertTrue(contract["rerank_after_every_material_run"])
        self.assertIn("insufficient", contract["minimum_material_output"])

    def test_steward_context_routes_progress_to_portfolio(self) -> None:
        context = (ROOT / "steward" / "README.md").read_text(encoding="utf-8")
        self.assertIn("steward/research-portfolio.json", context)
        self.assertIn(self.data["north_star_lane"], context)
        active = next(lane for lane in self.data["lanes"] if lane["state"] == "ACTIVE")
        self.assertIn("ADAPTER2-01", active["current_authority"])
        adapter = next(
            item
            for item in active["internal_work_items"]
            if item["id"] == "P2C-BOUNDARY-ADAPTER"
        )
        self.assertIn("Do not repeat the 2026-07-16c QIP fixture", adapter["next_swing"])


if __name__ == "__main__":
    unittest.main()
