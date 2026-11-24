#!/usr/bin/env python3
"""One Line, One Chill - make.fun entry.

Writes a single horror sentence (under 200 characters) to /output/entry.txt.
Deterministic: the same line on every run. No network, no randomness, no input.
"""

import os

LINE = "The ultrasound showed two heartbeats, and the doctor smiled and said, 'Yours stopped an hour ago.'"


def main() -> None:
    # Self-check against the competition gate: UTF-8 text, 1-200 chars,
    # not only white space, exactly one sentence.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only white space"
    assert LINE.count(".") == 1 and LINE.rstrip("'").endswith("."), "line must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
