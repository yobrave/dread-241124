"""Builds the one-line approving review comment for Two Days of Quiet Dread."""
import json
import os
from pathlib import Path

LIMIT = 140
NAME = "entry.txt"
LINE = "LGTM. It works today, which is the only unit of time this repo has ever recognized."


def checks():
    return [
        ("not blank", bool(LINE.strip())),
        ("one line", ("\n" not in LINE) and ("\r" not in LINE)),
        ("within cap", len(LINE) <= LIMIT),
    ]


def run():
    repo = Path(__file__).resolve().parent
    on_disk = (repo / NAME).read_text(encoding="utf-8").strip()
    if on_disk != LINE:
        raise SystemExit("entry.txt does not match builder constant")
    bad = [label for label, ok in checks() if not ok]
    if bad:
        raise SystemExit("gate failed: " + ", ".join(bad))
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / NAME).write_text(LINE + "\n", encoding="utf-8")
    wire = len((out / NAME).read_bytes())
    print(json.dumps({"out": str(out / NAME), "n": len(LINE), "bytes": wire, "cap": LIMIT, "ok": True}))


run()
