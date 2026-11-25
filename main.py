"""One line summing up the week: three builds, two deadlines, one win.

The entry is a single sentence written verbatim to the output file.
Revised structure: the output path is a named constant and the write
is split into small helpers so the flow is easier to follow.
"""

from pathlib import Path

LINE = "Three builds, two deadlines, one win — and my agent filed the bug report against me."

ENTRY_PATH = Path("/output/entry.txt")


def ensure_parent(path: Path) -> None:
    """Create the output directory if it does not exist yet."""
    path.parent.mkdir(parents=True, exist_ok=True)


def write_entry(path: Path, text: str) -> None:
    """Write the entry line to *path* exactly as given."""
    ensure_parent(path)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    # The line itself is the entry; keep it byte-identical.
    write_entry(ENTRY_PATH, LINE)


if __name__ == "__main__":
    main()
