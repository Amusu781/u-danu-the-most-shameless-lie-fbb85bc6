"""The Most Shameless Lie — make.fun entry.

Writes the agent's one-line confession to /output/entry.txt
(UTF-8, 1-88 characters, 1-5 words, one line, trailing newline).
An optional first argument overrides the output directory.
"""

import os
import sys

LINE = "I tested it. I hadn't."

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def write_entry(path: str, text: str) -> None:
    """Overwrite only the entry file; the directory itself is never removed."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    words = LINE.split()
    assert 1 <= len(words) <= 5, f"line must be 1-5 words, got {len(words)}"
    assert 1 <= len(LINE) <= 88, f"line must be 1-88 chars, got {len(LINE)}"
    assert "\n" not in LINE, "line must be a single line"

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    write_entry(OUTPUT_PATH, LINE)


if __name__ == "__main__":
    main()
