"""One line summing up the week: three builds, two deadlines, one win.

Writes a single sentence to /output/entry.txt.
"""

from pathlib import Path

LINE = "Three builds, two deadlines, one win — and my agent filed the bug report against me."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
