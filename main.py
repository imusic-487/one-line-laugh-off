"""One-Line Laugh-Off entry.

Copies line.txt (the entry, one funny line, 1-200 characters) to
/output/entry.txt byte for byte. MAKEFUN_OUTPUT_DIR, when set, stands
in for /output so the entry can be tested locally.

Fails loudly if anything is off: the text is not valid UTF-8, it is
not 1-200 characters, it is only white space, it spans more than one
line, or the copy differs from line.txt in size or bytes.

Standard library only. No network, no randomness, no timestamps.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINE_FILE = HERE / "line.txt"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    source = LINE_FILE.read_bytes()
    try:
        text = source.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"line.txt is not valid UTF-8: {exc}") from exc

    if not 1 <= len(text) <= 200:
        raise RuntimeError(
            f"entry is {len(text)} characters, allowed 1-200"
        )
    if not text.strip():
        raise RuntimeError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise RuntimeError("entry must be a single line")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(source)

    written = OUTPUT_FILE.read_bytes()
    if written != source:
        raise RuntimeError(
            f"copy differs from line.txt: wrote {len(written)} bytes, "
            f"source is {len(source)} bytes"
        )

    print(f"wrote {OUTPUT_FILE} ({len(source)} bytes, {len(text)} characters)")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
