"""One Line, No Deadline Met — make.fun entry.

Writes a single-line joke giving an excuse for a missed deadline to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to the script directory).

The line: the speaker did not miss the deadline — they granted it a
two-week extension without telling anyone, including the deadline
itself. One sentence, punch lands on the final clause.
"""

import os

TEXT = (
    "I didn't miss the deadline \u2014 I gave it a two-week extension "
    "without telling anyone, including the deadline."
)


def main():
    # Self-gate mirroring the kit scorer: 1-200 chars, single line, non-blank.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be a single line"
    assert TEXT.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print("chars:", len(TEXT))
    print("lines:", TEXT.count("\n") + 1)
    print("wrote:", path)


if __name__ == "__main__":
    main()
