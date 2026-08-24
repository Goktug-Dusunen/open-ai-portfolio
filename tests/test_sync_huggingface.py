from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sync_huggingface", ROOT / "scripts" / "sync_huggingface.py")
SYNC = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(SYNC)


class RenderSnapshotTests(unittest.TestCase):
    def setUp(self) -> None:
        artifact = {
            "id": "GoktugD/example-model",
            "url": "https://huggingface.co/GoktugD/example-model",
            "task": "text-generation",
            "downloads": 1234,
            "likes": 5,
            "last_modified": "2026-08-24T00:00:00Z",
        }
        empty = {"models": [], "datasets": [], "spaces": []}
        self.catalog = {
            "generated_at": "2026-08-24T00:00:00+00:00",
            "owners": {
                "GoktugD": {**empty, "models": [artifact]},
                "Werea-co": dict(empty),
            },
        }

    def test_snapshot_contains_metrics_and_model(self) -> None:
        snapshot = SYNC.render_snapshot(self.catalog)
        self.assertIn("| 1 | 0 | 0 | 1,234 |", snapshot)
        self.assertIn("GoktugD/example-model", snapshot)
        self.assertTrue(snapshot.startswith(SYNC.START_MARKER))
        self.assertTrue(snapshot.endswith(SYNC.END_MARKER))

    def test_artifact_kinds_are_stable(self) -> None:
        self.assertEqual(SYNC.KINDS, ("models", "datasets", "spaces"))


if __name__ == "__main__":
    unittest.main()
