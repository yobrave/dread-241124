"""Quiet Dread code-review comment: gate + export runner (round 4)."""
import json
import pathlib
import shutil

CAP = 140
HERE = pathlib.Path(__file__).resolve().parent
SLUGCODE = "drd4-quiet-dread-r4"


class Shipper:
    def __init__(self, root):
        self.src = root / "entry.txt"
        self.outdir = root / "out"

    def validate(self, text):
        stripped = text.strip()
        assert 1 <= len(stripped) <= CAP, "gate length"
        return len(stripped)

    def run(self):
        text = self.src.read_text(encoding="utf-8")
        n = self.validate(text)
        self.outdir.mkdir(exist_ok=True)
        shutil.copyfile(self.src, self.outdir / "entry.txt")
        return {"verdict": "shipped", "code": SLUGCODE, "chars": n, "cap": CAP}


if __name__ == "__main__":
    print(json.dumps(Shipper(HERE).run()))
