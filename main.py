"""Cat-joke entry writer.

Builds the single-line entry for the "one-line cat joke" bounty and
stores it at /output/entry.txt exactly as required: one line, UTF-8,
no trailing newline.
"""

import os


ENTRY = (
    "My cat deleted my work by sitting on the keyboard, then stared at "
    "me like I was the one who didn't understand the assignment."
)


def check_entry(text):
    """Raise ValueError unless *text* is a usable one-line entry.

    A usable entry is a non-blank string of 1-200 characters with no
    line breaks in it, so it always fits on exactly one line.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be between 1 and 200 characters")


def write_entry(text, path="/output/entry.txt"):
    """Write *text* to *path* as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main():
    check_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
