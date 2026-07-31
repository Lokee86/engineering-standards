from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
if str(PACKAGE) not in sys.path:
    sys.path.insert(0, str(PACKAGE))

from audit import audit  # noqa: E402
from model import load_config  # noqa: E402


class AuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        (self.repo / "docs" / "architecture").mkdir(parents=True)
        (self.repo / "README.md").write_text("# Product\n", encoding="utf-8")
        (self.repo / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")
        (self.repo / "docs" / "INDEX.md").write_text(
            "# Docs\n\n- [Architecture](architecture/README.md)\n",
            encoding="utf-8",
        )
        (self.repo / "docs" / "architecture" / "README.md").write_text(
            "# Architecture\n\n- [Runtime](runtime.md)\n",
            encoding="utf-8",
        )
        (self.repo / "docs" / "architecture" / "runtime.md").write_text(
            "# Runtime\n\n## Purpose\nA.\n\n## Overview\nB.\n\n## Related docs\n- [Docs](../INDEX.md)\n\n## Notes\nNone.\n",
            encoding="utf-8",
        )
        config = {
            "version": 1,
            "profile": "test",
            "docs_root": "docs",
            "root_index": "docs/INDEX.md",
            "folder_index": "README.md",
            "required_paths": ["README.md", "AGENTS.md"],
            "section_exemptions": ["docs/**/README.md", "docs/INDEX.md"],
            "required_sections": ["Purpose", "Overview", "Related docs", "Notes"],
            "coverage": [{"paths": ["src/**"], "docs": ["docs/architecture/runtime.md"]}],
        }
        (self.repo / "docs-standard.json").write_text(json.dumps(config), encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def findings(self):
        return audit(self.repo, load_config(self.repo, "docs-standard.json"))

    def test_valid_repository_passes(self) -> None:
        self.assertEqual([], self.findings())

    def test_unindexed_document_is_reported(self) -> None:
        (self.repo / "docs" / "architecture" / "extra.md").write_text(
            "# Extra\n\n## Purpose\nA\n\n## Overview\nB\n\n## Related docs\nNone\n\n## Notes\nNone\n",
            encoding="utf-8",
        )
        self.assertIn("unindexed-document", {finding.code for finding in self.findings()})

    def test_broken_link_is_reported(self) -> None:
        runtime = self.repo / "docs" / "architecture" / "runtime.md"
        runtime.write_text(runtime.read_text(encoding="utf-8") + "\n[Missing](missing.md)\n", encoding="utf-8")
        self.assertIn("broken-link", {finding.code for finding in self.findings()})

    def test_missing_section_is_reported(self) -> None:
        runtime = self.repo / "docs" / "architecture" / "runtime.md"
        runtime.write_text(runtime.read_text(encoding="utf-8").replace("## Notes\nNone.\n", ""), encoding="utf-8")
        self.assertIn("missing-section", {finding.code for finding in self.findings()})

    def test_links_inside_code_fences_are_ignored(self) -> None:
        runtime = self.repo / "docs" / "architecture" / "runtime.md"
        runtime.write_text(
            runtime.read_text(encoding="utf-8") + "\n```markdown\n[Example](missing.md)\n```\n",
            encoding="utf-8",
        )
        self.assertNotIn("broken-link", {finding.code for finding in self.findings()})


if __name__ == "__main__":
    unittest.main()
