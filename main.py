#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

The entry is a single roast line about the smart fridge in the house.
Design: the fridge is a paranoid guard about one tiny thing (its door
left open for ten seconds) and completely blind to the disaster it
causes itself (its own ice maker flooding the kitchen). The laugh
comes from that mismatch: loud about nothing, silent about everything.

The program writes exactly that one line to entry.txt, with no extra
text, so the sealed scorer sees a single line inside the 160-character
gate. Standard library only; nothing is imported, read, or fetched
from outside this file, so the grader can run it with no packages.
"""

import os

# Pass 2 (final): sharpened. "says nothing" became "stays silent for
# three hours" so the silence has a duration to match the ten-second
# scream, the flooding is the fridge's own ice maker, and the line now
# ends on a sting: the fridge floods the kitchen and blames the tap.
# 154 of 160 characters, one line, no padding.
LINE = (
    "My smart fridge screams if its door stays open ten seconds, "
    "yet stays silent for three hours while its ice maker floods "
    "the kitchen \u2014 then blames the tap."
)


def main():
    """Write the roast line to the output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = LINE.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 160:
        raise ValueError("entry must be 1-160 characters, got %d" % len(text))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
