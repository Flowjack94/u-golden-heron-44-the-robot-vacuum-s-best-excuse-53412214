#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun bounty entry.

Writes one line, at most 140 characters, to /output/entry.txt:
the funniest excuse a robot vacuum gives for missing a spot.
Standard library only; no network; reads nothing outside the repo.
"""

import os
import sys

ENTRY = (
    "I left that crumb on purpose — my cliff sensor swore it was a "
    "staircase, and I don't fall down stairs for a Cheerio."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Return True only if text is a valid one-line entry.

    Rules: str, 1-140 characters, not only whitespace, single line,
    no C1 control characters, no U+FFFD replacement character and no
    lone surrogates.
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 140:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text or "\t" in text:
        return False
    for ch in text:
        code = ord(ch)
        if 0x80 <= code <= 0x9F:  # C1 control characters
            return False
        if code == 0xFFFD:  # replacement character
            return False
        if 0xD800 <= code <= 0xDFFF:  # lone surrogates
            return False
        if code < 0x20:  # any C0 control character
            return False
    return True


def main():
    if not validate_entry(ENTRY):
        print("error: entry failed validation", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    # Round-trip check: what landed on disk must be exactly the entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY or not validate_entry(written):
        print("error: round-trip check failed", file=sys.stderr)
        return 1
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
