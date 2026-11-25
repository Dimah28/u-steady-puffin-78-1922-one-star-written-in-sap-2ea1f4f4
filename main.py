#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry generator.

Writes a single one-line, 1-star review from a houseplant about its human
owner to $MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only, deterministic, no
network. SPDX-License-Identifier: MIT
"""

import os
import sys

ENTRY_TEXT = (
    "One star. He waters me with cold coffee, hides me behind the TV for "
    "'ambience,' then calls me his thriving jungle. I've seen sunlight "
    "twice and I'm now interviewing new owners."
)

MIN_LEN = 1
MAX_LEN = 279

OUTPUT_FILENAME = "entry.txt"


def _validate_entry(text: str) -> list[str]:
    """Check the entry against the bounty gates.

    Returns a list of human-readable problems; empty means the entry is
    valid. Rules: 1-279 characters, exactly one line, not only whitespace.
    """
    problems: list[str] = []
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        problems.append(
            f"entry length {len(text)} outside {MIN_LEN}-{MAX_LEN}"
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if not text.strip():
        problems.append("entry must not be only whitespace")
    return problems


def _resolve_output_dir() -> str | None:
    """Return the output directory from the environment, or None."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR")


def _write_entry(text: str, out_dir: str) -> str:
    """Write the validated entry to entry.txt; return the full path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return path


def main() -> int:
    out_dir = _resolve_output_dir()
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    problems = _validate_entry(ENTRY_TEXT)
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1

    _write_entry(ENTRY_TEXT, out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
