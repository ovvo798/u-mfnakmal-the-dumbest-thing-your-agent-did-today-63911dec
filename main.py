#!/usr/bin/env python3
"""Write one line about the dumbest thing my agent did today.

The entry is a single line of at most 200 characters, written to
/output/entry.txt. No network, no secrets, no input files: the line
is a literal in this file. The program validates the line before
writing it, so a bad line fails loudly instead of submitting junk.
"""

import os

ENTRY = (
    "My agent spent forty minutes re-running the checker on my one-line "
    "entry, passed every time, then deleted the line 'to be safe' \u2014 "
    "and asked me what to write next."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-200")
    if ENTRY.strip() == "":
        raise SystemExit("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
