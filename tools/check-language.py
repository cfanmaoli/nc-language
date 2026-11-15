#!/usr/bin/env python3
"""Validate a Nimble Commander-Fork language pack.

Usage:
    python3 tools/check-language.py languages/<code>.json [languages/en.json]

Checks the pack structure, reports entries that are missing relative to the reference and how much
of the file is translated. Exit code 0 means the file is a structurally valid pack.
"""

import json
import sys
from pathlib import Path

FORMAT = "nimble-commander-language-pack"
FIELDS = ("bundle", "table", "key", "source", "translation")


def load(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def key_of(entry):
    return (entry.get("bundle", ""), entry.get("table", ""), entry.get("key", ""))


def main(argv):
    if len(argv) not in (2, 3):
        print(__doc__.strip())
        return 2

    target = Path(argv[1])
    reference = Path(argv[2]) if len(argv) == 3 else Path(__file__).resolve().parent.parent / "languages" / "en.json"
    if not target.is_file():
        print(f"error: {target} does not exist")
        return 1
    if not reference.is_file():
        print(f"error: reference file {reference} does not exist")
        return 1

    try:
        data = load(target)
        ref = load(reference)
    except json.JSONDecodeError as error:
        print(f"error: invalid JSON: {error}")
        return 1

    errors = []
    if data.get("format") != FORMAT:
        errors.append(f'"format" must be "{FORMAT}"')
    if data.get("formatVersion") != 1:
        errors.append('"formatVersion" must be 1')
    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        errors.append('"entries" must be a non-empty array')
        entries = []

    print(f"language: {data.get('language', '?')} ({data.get('languageName', '?')})")
    print(f"entries:  {len(entries)}")

    seen = set()
    translated = 0
    empty = 0
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"entry {index} is not an object")
            continue
        for field in FIELDS:
            if not isinstance(entry.get(field), str):
                errors.append(f"entry {index}: '{field}' must be a string")
        identifier = key_of(entry)
        if identifier in seen:
            errors.append(f"duplicate entry {identifier}")
        seen.add(identifier)
        if entry.get("translation"):
            translated += 1
        else:
            empty += 1

    reference_keys = {key_of(entry) for entry in ref.get("entries", [])}
    missing = reference_keys - seen
    extra = seen - reference_keys
    print(f"translated: {translated}")
    print(f"empty:      {empty}")
    print(f"missing:    {len(missing)}")
    if extra:
        print(f"extra:      {len(extra)} (keys not present in {reference.name})")
        for identifier in sorted(extra)[:10]:
            print("  ", identifier)
    if missing:
        for identifier in sorted(missing)[:10]:
            print("   missing:", identifier)

    if errors:
        print("")
        for error in errors:
            print("error:", error)
        return 1

    print("")
    print("ok: the file is a valid language pack")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
