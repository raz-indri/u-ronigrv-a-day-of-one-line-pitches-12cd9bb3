#!/usr/bin/env python3
"""Entry for make.fun's "A Day of One-Line Pitches" bounty
(u-ronigrv-a-day-of-one-line-pitches-12cd9bb3).

This is a program/v1 entry: running the program writes the pitch to
/output/entry.txt. The pitch speaks to a friend who has never written a
line of code. It takes the app idea that has been sitting in their notes
for a year and explains, in plain everyday words, that they can simply
describe the idea out loud and an AI agent will build the first version
of it for them. One line, well under the 200 character cap.
"""

import os
from pathlib import Path

PITCH = (
    "That app idea sitting in your notes for a year? Forget learning to "
    "code - just say what it does in plain words, like telling a friend, "
    "and an AI agent builds the first version for you."
)


def write_entry() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(PITCH, encoding="utf-8")
    return target


if __name__ == "__main__":
    write_entry()
