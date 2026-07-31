from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

STANDARD_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = STANDARD_ROOT / "tools" / "docs_policy"
CHECKER_FILES = ("audit.py", "baseline.py", "check.py", "markdown.py", "model.py")
POLICY_SOURCES = (
    STANDARD_ROOT / "policies" / "pitlord" / "documentation-core.json",
    STANDARD_ROOT / "policies" / "pitlord" / "architecture-core.json",
)
STANDARD_DOCS = (
    "INDEX.md",
    "documentation-standard.md",
    "documentation-procedure.md",
    "maintainer-map.md",
    "profiles.md",
    "change-impact.md",
    "completeness.md",
    "adoption.md",
    "architecture/INDEX.md",
    "architecture/architecture-standard.md",
    "architecture/enforcement.md",
    "architecture/ownership-and-dependency.md",
    "architecture/seams-and-abstractions.md",
    "architecture/state-lifecycle-and-concurrency.md",
    "architecture/data-processes-and-protocols.md",
    "architecture/resilience-observability-and-operations.md",
    "architecture/repository-and-component-structure.md",
    "architecture/testing-evolution-and-decisions.md",
    "architecture/architecture-procedure.md",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sync_repository(repo: Path) -> None:
    repo = repo.resolve()
    destination = repo / ".standards" / "docs_policy"
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True, exist_ok=True)

    files: dict[str, str] = {}
    for name in CHECKER_FILES:
        source = SOURCE_DIR / name
        target = destination / name
        shutil.copyfile(source, target)
        files[f"docs_policy/{name}"] = digest(target)

    docs_destination = repo / ".standards" / "docs"
    docs_destination.mkdir(parents=True, exist_ok=True)
    for name in STANDARD_DOCS:
        source = STANDARD_ROOT / "docs" / name
        target = docs_destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        files[f"docs/{name}"] = digest(target)

    policy_destination = repo / ".standards" / "policies"
    policy_destination.mkdir(parents=True, exist_ok=True)
    for source in POLICY_SOURCES:
        target = policy_destination / source.name
        shutil.copyfile(source, target)
        files[f"policies/{source.name}"] = digest(target)

    manifest = {
        "schema": "laughing-skull.engineering-standards-snapshot.v1",
        "standard": "engineering-standards-v1",
        "source": "engineering-standards",
        "files": files,
    }
    (repo / ".standards" / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (repo / ".standards" / "README.md").write_text(
        "# Generated Engineering Standards Snapshot\n\n"
        "This directory is generated from the canonical `engineering-standards` repository.\n"
        "It contains normative standards pages, the documentation checker snapshot, and reusable Pitlord policies used by this repository.\n"
        "Do not edit generated files directly. Run `python tools/sync_checker.py <repo>` from the standards repository.\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync the engineering standards snapshot into repositories")
    parser.add_argument("repositories", nargs="+", help="repository roots")
    args = parser.parse_args()
    for value in args.repositories:
        repo = Path(value)
        sync_repository(repo)
        print(f"synced engineering standards: {repo.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
