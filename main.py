#!/usr/bin/env python3
"""Write exactly one word — AGLET — to entry.txt.

AGLET is the little plastic or metal tip at the end of a shoelace:
seen by everyone, named by almost no one. The program writes it, and
only it, to entry.txt inside the directory named by MAKEFUN_OUTPUT_DIR.
"""

import os
import sys

WORD = "AGLET"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
