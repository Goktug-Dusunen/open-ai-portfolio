#!/usr/bin/env python3
"""Synchronize public Hugging Face artifacts into a GitHub-friendly catalog."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "portfolio.json"
README_PATH = ROOT / "README.md"
OWNERS = ("GoktugD", "Werea-co")
KINDS = ("models", "datasets", "spaces")
START_MARKER = "<!-- portfolio:start -->"
END_MARKER = "<!-- portfolio:end -->"


def fetch_public_artifacts(owner: str, kind: str) -> list[dict]:
    query = urlencode({"author": owner, "limit": 100, "full": "true"})
    request = Request(
        f"https://huggingface.co/api/{kind}?{query}",
        headers={"User-Agent": "goktug-open-ai-portfolio/1.0"},
    )
    with urlopen(request, timeout=30) as response:
        payload = json.load(response)

    artifacts = []
    for item in payload:
        artifact_id = item["id"]
        namespace = "spaces/" if kind == "spaces" else "datasets/" if kind == "datasets" else ""
        artifacts.append(
            {
                "id": artifact_id,
                "url": f"https://huggingface.co/{namespace}{artifact_id}",
                "task": item.get("pipeline_tag"),
                "downloads": item.get("downloads") or 0,
                "likes": item.get("likes") or 0,
                "last_modified": item.get("lastModified"),
            }
        )
    return sorted(artifacts, key=lambda artifact: artifact["id"].casefold())


def build_catalog() -> dict:
    owners = {
        owner: {kind: fetch_public_artifacts(owner, kind) for kind in KINDS}
        for owner in OWNERS
    }
    previous = {}
    if DATA_PATH.exists():
        try:
            previous = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            previous = {}

    generated_at = previous.get("generated_at")
    if previous.get("owners") != owners or not generated_at:
        generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    return {"generated_at": generated_at, "owners": owners}


def render_snapshot(catalog: dict) -> str:
    lines = [
        START_MARKER,
        "",
        "## Current snapshot",
        "",
        f"Last synchronized: `{catalog['generated_at']}`",
        "",
        "| Publisher | Models | Datasets | Spaces | Downloads |",
        "|---|---:|---:|---:|---:|",
    ]

    for owner, artifacts in catalog["owners"].items():
        downloads = sum(
            artifact["downloads"]
            for kind in KINDS
            for artifact in artifacts[kind]
        )
        lines.append(
            f"| [{owner}](https://huggingface.co/{owner}) "
            f"| {len(artifacts['models'])} | {len(artifacts['datasets'])} "
            f"| {len(artifacts['spaces'])} | {downloads:,} |"
        )

    models = [
        model
        for artifacts in catalog["owners"].values()
        for model in artifacts["models"]
    ]
    models.sort(
        key=lambda model: (model["downloads"], model["likes"], model["id"]),
        reverse=True,
    )
    lines.extend(
        [
            "",
            "## Most-used models",
            "",
            "| Model | Task | Downloads | Likes |",
            "|---|---|---:|---:|",
        ]
    )
    for model in models[:10]:
        task = model["task"] or "—"
        lines.append(
            f"| [{model['id']}]({model['url']}) | {task} "
            f"| {model['downloads']:,} | {model['likes']:,} |"
        )

    lines.extend(["", END_MARKER])
    return "\n".join(lines)


def update_readme(catalog: dict) -> None:
    readme = README_PATH.read_text(encoding="utf-8")
    if START_MARKER not in readme or END_MARKER not in readme:
        raise RuntimeError("README portfolio markers are missing")
    prefix, remainder = readme.split(START_MARKER, 1)
    _, suffix = remainder.split(END_MARKER, 1)
    README_PATH.write_text(
        prefix.rstrip() + "\n\n" + render_snapshot(catalog) + suffix,
        encoding="utf-8",
    )


def main() -> None:
    catalog = build_catalog()
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    update_readme(catalog)
    total = sum(
        len(artifacts[kind])
        for artifacts in catalog["owners"].values()
        for kind in KINDS
    )
    print(f"Synchronized {total} public artifacts")


if __name__ == "__main__":
    main()
