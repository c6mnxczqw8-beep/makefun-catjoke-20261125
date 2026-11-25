#!/usr/bin/env python3
"""Entry program for The One-Line Cat Joke That Lands.

Writes one cat joke (under 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
The joke is about supervision: the cat has reviewed your
work, at 3 a.m., from on top of it.
"""

import os

LINE = (
    "My cat called a family meeting by sitting in the "
    "suitcase: agenda, one item; decision, also one."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
