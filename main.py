#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes one original excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure Python standard library, deterministic:
the same line on every run.
"""

import os
import sys

MAX_CHARS = 200
ENTRY_FILENAME = "entry.txt"

EXCUSE = (
    "I missed the deadline because I trained on your last 400 messages "
    "and learned, with 94% confidence, that you'd forgive me."
)


def main() -> int:
    line = EXCUSE
    if not line or not line.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: entry is %d chars, over the %d limit" % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(
        os.path.join(out_dir, ENTRY_FILENAME), "w", encoding="utf-8", newline=""
    ) as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
