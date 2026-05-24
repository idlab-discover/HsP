#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent


def count(pattern: str) -> int:
    return len(list(ROOT.glob(pattern)))


def main() -> int:
    checks = {
        "scenario YAML files": (
            count("artifacts/scenarios/**/*.yaml"),
            47,
        ),
        "processed parquet datasets": (
            count("artifacts/data/**/*.parquet"),
            13,
        ),
        "curated notebooks": (
            count("artifacts/ml-evaluation/notebooks/**/*.ipynb"),
            6,
        ),
        "result CSV files": (
            count("artifacts/ml-evaluation/results/**/*_results.csv"),
            78,
        ),
    }

    errors: list[str] = []

    for label, (actual, expected) in checks.items():
        if actual != expected:
            errors.append(f"{label}: expected {expected}, found {actual}")

    raw_pcaps = list(ROOT.glob("artifacts/data/realistic-raw/**/*.pcap"))
    if raw_pcaps:
        errors.append(
            "raw packet captures should not be present in the public branch: "
            + ", ".join(str(path.relative_to(ROOT)) for path in raw_pcaps)
        )

    if errors:
        print("Artifact check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Artifact check passed.")
    for label, (actual, _) in checks.items():
        print(f"- {label}: {actual}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
