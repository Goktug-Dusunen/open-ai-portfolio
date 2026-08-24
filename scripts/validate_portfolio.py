#!/usr/bin/env python3
"""Validate the generated catalog and static website contract."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "portfolio.json"
DOCS_CATALOG_PATH = ROOT / "docs" / "portfolio.json"
KINDS = ("models", "datasets", "spaces")
REQUIRED_ARTIFACT_FIELDS = {"id", "url", "task", "downloads", "likes", "last_modified"}


def validate() -> int:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    docs_catalog = json.loads(DOCS_CATALOG_PATH.read_text(encoding="utf-8"))
    if catalog != docs_catalog:
        raise ValueError("data/portfolio.json and docs/portfolio.json differ")
    if not catalog.get("generated_at") or not catalog.get("owners"):
        raise ValueError("catalog metadata is incomplete")

    total = 0
    for owner, kinds in catalog["owners"].items():
        if set(kinds) != set(KINDS):
            raise ValueError(f"{owner} has unexpected artifact kinds")
        for kind, artifacts in kinds.items():
            ids = [artifact["id"] for artifact in artifacts]
            if len(ids) != len(set(ids)):
                raise ValueError(f"duplicate IDs in {owner}/{kind}")
            for artifact in artifacts:
                if set(artifact) != REQUIRED_ARTIFACT_FIELDS:
                    raise ValueError(f"invalid fields for {artifact.get('id')}")
                parsed = urlparse(artifact["url"])
                if parsed.scheme != "https" or parsed.netloc != "huggingface.co":
                    raise ValueError(f"invalid URL for {artifact['id']}")
                if artifact["downloads"] < 0 or artifact["likes"] < 0:
                    raise ValueError(f"negative metrics for {artifact['id']}")
            total += len(artifacts)

    for required in ("index.html", "styles.css", "app.js", "favicon.svg"):
        if not (ROOT / "docs" / required).is_file():
            raise ValueError(f"missing website asset: {required}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if readme.count("<!-- portfolio:start -->") != 1 or readme.count("<!-- portfolio:end -->") != 1:
        raise ValueError("README synchronization markers are invalid")
    return total


if __name__ == "__main__":
    print(f"Validated {validate()} public artifacts")
