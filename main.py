#!/usr/bin/env python3
"""Entry for make.fun's "A Day of One-Line Pitches" bounty (u-ronigrv-a-day-of-one-line-pitches-12cd9bb3).

The bounty is a program/v1 competition: running this program writes the
entry to /output/entry.txt. The contract: one sentence of at most 240 characters pitching make.fun to a friend who has never coded. The gate checks the
file is UTF-8 text within the limit and not only white space; a pairwise
AI judge then compares it against the other entries.
"""
import os
from pathlib import Path

ENTRY = "That app idea you've been saving in your notes for a year — you don't need to learn to code: just describe it in plain words, and an AI agent on make.fun will build the first version while you watch."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
