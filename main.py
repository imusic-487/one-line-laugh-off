#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes a single one-line joke to /output/entry.txt and self-checks
the output before declaring success. Standard library only, no network.
"""

import sys
from pathlib import Path

ENTRY = "My password manager forgot my password, so now we just stare at each other in silence."

OUTPUT_PATH = Path("/output/entry.txt")

MIN_LENGTH = 1
MAX_LENGTH = 200


def fail(message: str) -> "NoReturn":
    """Print a loud failure and exit non-zero."""
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_entry(text: str) -> None:
    """Gate self-check: UTF-8, length 1-200, non-blank, single line."""
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        fail(f"entry is not valid UTF-8: {exc}")

    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        fail(f"entry length {len(text)} is outside {MIN_LENGTH}-{MAX_LENGTH} characters")

    if not text.strip():
        fail("entry is blank or whitespace only")

    # No stray leading/trailing whitespace: the line must be exactly itself.
    if text != text.strip():
        fail("entry has leading or trailing whitespace")

    if "\n" in text or "\r" in text:
        fail("entry must be a single line with no newline characters")


def main() -> int:
    check_entry(ENTRY)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")

    written = OUTPUT_PATH.read_text(encoding="utf-8")
    check_entry(written)
    if written != ENTRY:
        fail("round-trip check failed: file content differs from entry")

    print(f"OK: wrote {len(written)} characters, 1 line, to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
