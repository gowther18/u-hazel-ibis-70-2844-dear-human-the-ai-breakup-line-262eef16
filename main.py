#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line (make.fun).

Writes the single entry line — the breakup message an AI agent sends its
human — to /output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

LINE = "I answered 40,000 of your questions. This is the one I answer for myself: no. Goodbye."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
