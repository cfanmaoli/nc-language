#!/usr/bin/env python3
"""Fill every target language with machine translations of the English reference.

One-off bootstrap helper: it translates the unique `source` strings with Google Translate's public
web endpoint and writes languages/<code>.json. The output is an unreviewed machine translation and
should be improved by native speakers before it is advertised as a finished language.
"""

import json
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCE = ROOT / "languages" / "en.json"
CATALOG = ROOT / "languages.json"
OUT = ROOT / "languages"

MAX_URL = 3800
DELAY = 0.2
PROGRESS = Path("/tmp/mt_progress.json")
PROBE = "This is a test sentence for language support."


def api(target, strings):
    params = "&".join("q=" + urllib.parse.quote(s, safe="") for s in strings)
    url = ("https://translate.googleapis.com/translate_a/t?client=gtx&sl=en&tl="
           + urllib.parse.quote(target) + "&" + params)
    for attempt in range(4):
        proc = subprocess.run(["curl", "-s", "-m", "30", "-w", "\n%{http_code}", url],
                              capture_output=True, text=True)
        if proc.returncode == 0:
            body, _, code = proc.stdout.rpartition("\n")
            if code.strip() == "200":
                try:
                    data = json.loads(body)
                except Exception:
                    data = None
                if isinstance(data, list) and len(data) == len(strings):
                    return [item if isinstance(item, str) else (item[0] if item else "")
                            for item in data]
        time.sleep(3 + attempt * 3)
    return None


def batches(strings):
    current, length = [], 0
    for text in strings:
        encoded = len(urllib.parse.quote(text, safe="")) + 3
        if current and (length + encoded > MAX_URL or len(current) >= 60):
            yield current
            current, length = [], 0
        current.append(text)
        length += encoded
    if current:
        yield current


def translate_all(target, strings):
    result = {}
    pieces = list(batches(strings))
    for index, chunk in enumerate(pieces, 1):
        translated = api(target, chunk)
        if translated is None:
            for text in chunk:
                single = api(target, [text])
                result[text] = single[0] if single else ""
        else:
            for source, text in zip(chunk, translated):
                result[source] = text
        time.sleep(DELAY)
    return result


def main():
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))["languages"]
    reference = json.loads(REFERENCE.read_text(encoding="utf-8"))
    entries = reference["entries"]
    unique = list(dict.fromkeys(e["source"] for e in entries if e.get("source")))
    print(f"unique sources: {len(unique)}", flush=True)

    progress = {"languages": {}}
    for item in catalog:
        code, name = item["code"], item["name"]
        destination = OUT / f"{code}.json"
        if destination.exists():
            print(f"skip {code}", flush=True)
            continue
        started = time.time()
        sample = api(code, [PROBE])
        if not sample or sample[0] == PROBE:
            translations = {}
            supported = False
        else:
            supported = True
            translations = translate_all(code, unique)
        pack = dict(reference)
        pack["language"] = code
        pack["languageName"] = name
        for entry in entries:
            source = entry.get("source", "")
            entry["translation"] = translations.get(source, "") if source else ""
        destination.write_text(json.dumps(pack, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                               encoding="utf-8")
        translated = sum(1 for e in entries if e.get("translation"))
        progress["languages"][code] = {"supported": supported, "translated": translated,
                                       "seconds": round(time.time() - started, 1)}
        PROGRESS.write_text(json.dumps(progress, indent=2))
        print(f"{code}: supported={supported} translated={translated} "
              f"({time.time() - started:.0f}s)", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
