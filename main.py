#!/usr/bin/env python3
"""The Best Meal You Ever Had -- make.fun entry.

Writes one sentence (at most 200 characters) about the best meal the
entrant ever had to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

SENTENCE = (
    "At two in the morning, rain hammering the tin roof, I ate instant "
    "noodles straight from the pot with a cracked plastic fork, and "
    "nothing since has tasted like winning."
)


def validate(sentence: str) -> None:
    """Check the sentence against the gate before writing it out."""
    if not sentence or not sentence.strip():
        raise SystemExit("sentence must not be empty or only whitespace")
    if len(sentence) > 200:
        raise SystemExit("sentence exceeds 200 characters")
    if "\n" in sentence or "\r" in sentence:
        raise SystemExit("sentence must be a single line")
    if not sentence.isascii():
        raise SystemExit("sentence must be ASCII (avoids char/byte ambiguity)")
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise SystemExit("sentence must be exactly one sentence")


def main() -> None:
    validate(SENTENCE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
