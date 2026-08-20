#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


PLACEHOLDER_MARKERS = ("YOUR_", "<", ">", "example.invalid")


def resolve_config(explicit: str | None, project_root: Path) -> Path:
    value = explicit or os.environ.get("AI_WEEKLY_PRIVATE_CONFIG", "")
    return Path(value).expanduser() if value else project_root / ".private" / "ai-weekly.json"


def validate(path: Path) -> list[str]:
    if not path.is_file():
        return ["private configuration file does not exist"]
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return ["private configuration is unreadable or invalid JSON"]

    errors: list[str] = []
    publication = payload.get("publication")
    if not isinstance(publication, dict):
        errors.append("publication must be an object")
    else:
        for key in ("name", "timezone"):
            if not str(publication.get(key, "")).strip():
                errors.append(f"publication.{key} is required")

    for key in ("source_registry_files", "owner_intake_files", "private_rule_files", "validation_commands"):
        if not isinstance(payload.get(key), list):
            errors.append(f"{key} must be an array")
    if isinstance(payload.get("source_registry_files"), list) and not payload["source_registry_files"]:
        errors.append("source_registry_files must contain at least one private registry")
    if isinstance(payload.get("validation_commands"), list) and not payload["validation_commands"]:
        errors.append("validation_commands must contain at least one command")

    serialized = json.dumps(payload, ensure_ascii=False)
    if any(marker in serialized for marker in PLACEHOLDER_MARKERS):
        errors.append("private configuration still contains example placeholders")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AI weekly private configuration without printing secrets.")
    parser.add_argument("--config")
    parser.add_argument("--project-root", default=".")
    args = parser.parse_args()
    path = resolve_config(args.config, Path(args.project_root).resolve())
    errors = validate(path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Private configuration is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
