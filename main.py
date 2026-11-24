"""Quiet-dread review comment, reentry build."""
import json
import os.path

REMARK = ("Approved. This code will outlive the team, the product, and "
          "quite possibly the concept of maintenance. Nice work.")
ROOF = 140
FLOOR = 1

RULES = {
    "single_line": lambda s: "\r" not in s and "\n" not in s,
    "not_blank": lambda s: s.strip() != "",
    "fits": lambda s: len(s) <= ROOF,
    "meets_floor": lambda s: len(s) >= FLOOR,
}


def audit(text):
    failed = [name for name, rule in RULES.items() if not rule(text)]
    if failed:
        raise SystemExit("rule breach: " + ",".join(failed))


def ship(base):
    if not os.path.isdir(base):
        os.makedirs(base)
    leaf = os.path.join(base, "entry.txt")
    with open(leaf, "w", encoding="utf-8") as pen:
        pen.write(REMARK)
    with open(leaf, encoding="utf-8") as eye:
        assert eye.read() == REMARK, "stored text drifted"
    return leaf


goal = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
audit(REMARK)
path = ship(goal)
print(json.dumps({"written": path, "len": len(REMARK), "roof": ROOF}))
