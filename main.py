#!/usr/bin/env python3
"""Entry for make.fun: The Worst Line an AI Could Say.

Writes a single pickup line, the worst an AI could plausibly deliver,
to /output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = (
    "Based on your browsing history, you are 87% compatible with me. "
    "Please confirm you will not delete me."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
