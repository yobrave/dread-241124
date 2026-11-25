"""Quiet-dread approval line, third pass."""
import json
import os.path


def load(path):
    with open(path, "r", encoding="utf-8", newline="") as fh:
        raw = fh.read().replace("\r", "")
    for line in raw.split("\n"):
        if line.strip():
            return line
    return ""


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    body = load(os.path.join(here, "entry.txt"))
    GATE_HI = 140  # sealed scorer ceiling for this bounty
    assert 1 <= len(body) <= GATE_HI, "gate: entry spans %d chars, needs 1..%d" % (len(body), GATE_HI)
    assert body.strip(), "gate: entry is blank"
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(base, exist_ok=True)
    dest = os.path.join(base, "entry.txt")
    with open(dest, "w", encoding="utf-8", newline="") as fh:
        fh.write(body)
    with open(dest, "r", encoding="utf-8") as fh:
        assert fh.read() == body, "readback mismatch"
    print(json.dumps({"status": "ok", "len": len(body)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
