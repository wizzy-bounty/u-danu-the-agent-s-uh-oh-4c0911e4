#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

Writes exactly one word to entry.txt inside the directory named by the
MAKEFUN_OUTPUT_DIR environment variable (falling back to /output when the
variable is not set). Python standard library only, no network, fully
deterministic: every run writes the same bytes.
"""

import os

WORD = "recalculating"


def main() -> None:
    word = WORD
    # Contract guard: exactly one word, 1-99 characters, no whitespace tricks.
    if not word or word.strip() != word or len(word.split()) != 1:
        raise SystemExit("entry word must be exactly one word")
    if not 1 <= len(word) <= 99:
        raise SystemExit("entry word must be 1-99 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
