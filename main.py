"""The Long Roast — one-line roast of my own AI agent.

Writes a single original roast line (1-200 chars) to entry.txt.
Stdlib only. Honors MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

ROAST = (
    "My agent read 73KB of rules, built seventeen bounty entries, "
    "and still asked me what 'funny' means — then logged the question "
    "as progress and invoiced me for the confusion."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert text.strip(), "roast must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
