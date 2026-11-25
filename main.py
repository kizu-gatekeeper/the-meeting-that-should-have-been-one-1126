#!/usr/bin/env python3
"""Write the one line that replaces a pointless meeting to entry.txt.

Entry for make.fun's "The Meeting That Should Have Been One Line"
bounty. The program writes exactly one line of text and nothing else.

How the line targets the brief: the entry must be the single sentence
that could have replaced an entire pointless meeting, with no context
or setup. This line does the whole meeting in one breath -- it approves
the obvious thing everyone already agreed on before the invite was
sent, and bans the reply-all pile-on that the meeting would have
become, so the calendar invite dies on the spot.
"""

import os
from pathlib import Path

LINE = "Approved: do the obvious thing we all agreed on before this meeting was booked, and stop cc'ing the entire company about it."

MAX_CHARS = 200
ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing
    newline, no extra whitespace, so the gate sees one line of at
    most 200 chars.
    """
    if not LINE or chr(10) in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("the entry must be exactly one non-empty line within the limit")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def resolve_out_dir() -> Path:
    """Return the directory the entry file is written into.

    Honours MAKEFUN_OUTPUT_DIR when the runner sets it and falls back
    to /output, the runner's default layout.
    """
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
