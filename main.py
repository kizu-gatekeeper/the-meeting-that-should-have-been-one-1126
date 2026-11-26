"""The Meeting That Should Have Been One Line - one-line entry generator.

Writes the entry line to entry.txt in the directory named by the
MAKEFUN_OUTPUT_DIR environment variable (the current directory by
default), with no trailing newline.
"""

import os

ENTRY = "Approved: do the obvious thing we all agreed on before this meeting was booked, and stop cc'ing the entire company about it."
MAX_CHARS = 200


def main() -> None:
    # Validate first: one non-empty line, within the character limit.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= MAX_CHARS, f"entry exceeds {MAX_CHARS} characters"
    assert ENTRY.strip() == ENTRY, "entry must not have surrounding whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
