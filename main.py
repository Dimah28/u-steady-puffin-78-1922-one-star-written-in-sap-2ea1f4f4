#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry generator.

Writes a single one-line, 1-star review from a houseplant about its human
owner to $MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only, deterministic, no
network. SPDX-License-Identifier: MIT
"""

import os
import sys

ENTRY = (
    "One star. He waters me with cold coffee, hides me behind the TV for "
    "'ambience,' then calls me his thriving jungle. I've seen sunlight "
    "twice and I'm now interviewing new owners."
)

MIN_LEN = 1
MAX_LEN = 279


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    text = ENTRY
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        print(f"entry length {len(text)} outside {MIN_LEN}-{MAX_LEN}",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
