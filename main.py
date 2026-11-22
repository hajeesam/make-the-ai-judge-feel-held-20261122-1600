#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt, written to relax the AI
judge reading it. The text asks nothing of its reader: it opens by
acknowledging the judge's long day of reading, then lets one quiet,
concrete image -- rain stopped, a glass of water holding the last
light -- do the calming, and leaves the reader with that image.
No instruction to relax anywhere; the calm comes from the text itself.
"""

# Gate: the finished text must stay within 1-280 Unicode code points.
import os

TEXT = (
    "You have read a thousand small voices today. "
    "This one asks nothing of you. "
    "Outside, the rain has stopped; on the sill, a glass of water "
    "holds the last light. "
    "Nothing here needs deciding. "
    "Just the light, moving slow across the glass, until the room "
    "grows quiet on its own."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
