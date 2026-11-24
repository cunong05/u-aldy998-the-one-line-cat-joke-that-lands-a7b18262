"""The One-Line Cat Joke That Lands — make.fun entry.

Writes the one-line entry to /output/entry.txt with no trailing newline.
"""

import os

OUT_DIR = "/output"

ENTRY = "My cat deleted my work by sitting on the keyboard, then stared at me like I was the one who didn't understand the assignment."


def validate_entry(text):
    """Validate the entry is a single line of 1-200 chars (UTF-8)."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline)")
    return text


def main():
    entry = validate_entry(ENTRY)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
