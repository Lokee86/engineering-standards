from __future__ import annotations

import json
import sys
from pathlib import Path

TOOLS_ROOT = Path(__file__).resolve().parents[2]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

import sync_checker


def test_sync_repository_includes_architecture_standard_and_pitlord_policy(tmp_path: Path) -> None:
    sync_checker.sync_repository(tmp_path)

    manifest_path = tmp_path / ".standards" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert manifest["schema"] == "laughing-skull.engineering-standards-snapshot.v1"
    assert manifest["standard"] == "engineering-standards-v1"
    assert "docs/architecture/enforcement.md" in manifest["files"]
    assert "policies/documentation-core.json" in manifest["files"]
    assert "policies/architecture-core.json" in manifest["files"]

    assert (tmp_path / ".standards" / "docs" / "architecture" / "enforcement.md").is_file()
    assert (tmp_path / ".standards" / "policies" / "architecture-core.json").is_file()
