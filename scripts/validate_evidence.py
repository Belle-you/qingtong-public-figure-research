#!/usr/bin/env python3
"""Validate a Qingtong evidence ledger without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


REQUIRED = {
    "id",
    "claim",
    "claim_type",
    "status",
    "confidence",
    "risk_category",
    "event_date",
    "source_title",
    "source_url",
    "source_publisher",
    "source_tier",
    "published_date",
    "direct_support",
    "counterevidence",
    "notes",
}
ALLOWED = {
    "claim_type": {"fact", "allegation", "opinion", "inference"},
    "status": {
        "verified",
        "credible-allegation",
        "disputed",
        "unverified",
        "cleared-or-corrected",
    },
    "confidence": {"high", "medium", "low"},
    "risk_category": {
        "legal-regulatory",
        "professional-conduct",
        "public-statements-values",
        "commercial-consumer",
        "reliability-consistency",
        "information-integrity",
        "positive-evidence",
    },
    "source_tier": {"A", "B", "C", "D"},
}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def valid_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_record(record: object, index: int) -> list[str]:
    prefix = f"record {index}"
    if not isinstance(record, dict):
        return [f"{prefix}: must be an object"]

    errors: list[str] = []
    missing = REQUIRED - record.keys()
    extra = record.keys() - REQUIRED
    if missing:
        errors.append(f"{prefix}: missing fields: {', '.join(sorted(missing))}")
    if extra:
        errors.append(f"{prefix}: unknown fields: {', '.join(sorted(extra))}")

    for field, allowed_values in ALLOWED.items():
        if field in record and record[field] not in allowed_values:
            errors.append(f"{prefix}: invalid {field}: {record[field]!r}")

    for field in ("event_date", "published_date"):
        value = record.get(field)
        if value and (not isinstance(value, str) or not DATE_RE.match(value)):
            errors.append(f"{prefix}: {field} must be YYYY-MM-DD or empty")

    if not valid_url(record.get("source_url")):
        errors.append(f"{prefix}: source_url must be an http(s) URL")

    for field in REQUIRED:
        if field in record and not isinstance(record[field], str):
            errors.append(f"{prefix}: {field} must be a string")

    if record.get("source_tier") == "D" and record.get("status") != "unverified":
        errors.append(f"{prefix}: Tier D sources must remain unverified")

    if record.get("claim_type") == "allegation" and record.get("status") == "verified":
        errors.append(
            f"{prefix}: an allegation cannot be verified merely as an allegation; "
            "rewrite the claim or change its status"
        )

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_evidence.py evidence.json", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    try:
        # utf-8-sig also accepts plain UTF-8 and handles Windows-created BOM files.
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if not isinstance(data, list):
        print("ERROR: ledger root must be a JSON array", file=sys.stderr)
        return 1

    errors: list[str] = []
    seen_ids: set[str] = set()
    for index, record in enumerate(data, start=1):
        errors.extend(validate_record(record, index))
        if isinstance(record, dict) and isinstance(record.get("id"), str):
            if record["id"] in seen_ids:
                errors.append(f"record {index}: duplicate id: {record['id']}")
            seen_ids.add(record["id"])

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1

    print(f"OK: {len(data)} evidence record(s) validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
