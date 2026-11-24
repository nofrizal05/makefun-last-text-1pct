#!/usr/bin/env python3
"""The Charger Is Across the Room.

Writes the last text someone sends at 1% battery to /output/entry.txt:
one line, 129 characters, funny and desperate about the phone dying
mid-sentence while the charger sits across the room.

Standard library only. Deterministic: every run writes the same line.
"""

import os

TEXT = (
    "Phone at 1%, so if this cuts off mid-sentence, just know the charger "
    "is across the room and I love you more than my battery does."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    # The text must stay exactly one line: no newline may sneak in.
    assert "\n" not in TEXT and "\r" not in TEXT
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT + "\n")
    print(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
