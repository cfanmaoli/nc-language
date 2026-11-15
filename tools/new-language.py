#!/usr/bin/env python3
"""Create a language pack skeleton from languages/en.json.

Usage:
    python3 tools/new-language.py <code>

<code> must be listed in languages.json. The generated file has every entry of the English
reference with an empty translation, so it falls back to English until the values are filled in.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "languages.json"
REFERENCE = ROOT / "languages" / "en.json"


def main(argv):
    if len(argv) != 2:
        print(__doc__.strip())
        return 2

    code = argv[1]
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    languages = {item["code"]: item for item in catalog["languages"]}
    if code not in languages:
        print(f"error: {code!r} is not listed in languages.json - check the code or add the language there")
        return 1

    destination = ROOT / "languages" / f"{code}.json"
    if destination.exists():
        print(f"error: {destination.relative_to(ROOT)} already exists")
        return 1

    pack = json.loads(REFERENCE.read_text(encoding="utf-8"))
    pack["language"] = code
    pack["languageName"] = languages[code]["name"]
    for entry in pack["entries"]:
        entry["translation"] = ""

    destination.write_text(json.dumps(pack, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                            encoding="utf-8")
    print(f"created {destination.relative_to(ROOT)}")
    print(f"translate the 'translation' fields, then run: python3 tools/check-language.py "
          f"{destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
