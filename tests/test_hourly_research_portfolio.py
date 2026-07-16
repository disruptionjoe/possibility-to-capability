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
        selectable = [
            item
            for item in active[0]["internal_work_items"]
            if item["hourly_eligible"]
            and item["state"] in ("READY", "ADVANCED_OPEN_FRONTIER",
                                  "RESOLVED_SCOPED_SURVIVOR")
        ]
        self.assertGreaterEqual(len(selectable), 1)
        # Explicit rank overrides raw priority_score. The first cross-domain
        # transfer fixture has advanced for current available frozen inputs, so
        # the next frontier returns to the strongest physical continuation.
        self.assertTrue(self.data["selection_contract"][
            "explicit_rank_field_overrides_priority_score"])
        selected = min(selectable, key=lambda item: item["rank"])
        self.assertEqual(
            selected["id"], "P2C-REAL-PHYSICAL-WITNESS"
        )
        self.assertIn("reach_swing_accounting_2026_07_16",
                      self.data["selection_contract"])

    def test_hard_core_and_doctrine_fields(self) -> None:
        self.assertIn("HARD-CORE.md", self.data["hard_core"]["statement_owner"])
        self.assertIn("reach swing", self.data["selection_contract"]["reach_swing_cadence"])
        for lane in self.data["lanes"]:
            self.assertTrue(lane.get("relation_to_hard_core"))
            for item in lane.get("internal_work_items", []):
                self.assertTrue(item.get("relation_to_hard_core"))

    def test_two_lane_typed_change_role_is_durable(self) -> None:
        self.assertEqual(len(self.data["lanes"]), 2)
        self.assertEqual(
            self.data["north_star_lane"], "HIERARCHY-FORCE-OR-FALSIFY"
        )
        contract = self.data["selection_contract"]
        self.assertIn("not a separate meta lane",
                      contract["no_third_lane_for_meta_role"])
        self.assertIn("not the scope", contract["physics_specimen_rule"])

        charter = (ROOT / "governance" / "CHARTER.md").read_text(
            encoding="utf-8"
        )
        hard_core = (ROOT / "governance" / "HARD-CORE.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("## Agent-Capability Role", charter)
        self.assertIn("typed change", charter.lower())
        self.assertIn("Physics is not the scope", charter)
        self.assertIn("## The P2C-specific agent capability", hard_core)

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
