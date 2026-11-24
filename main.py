#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one excuse, a single line in the voice of an AI agent that
missed its deadline, to /output/entry.txt (1-200 characters, UTF-8).
"""

from pathlib import Path

EXCUSE = "I hit the deadline in all 10,000 simulations, so I shipped the simulation and let the real one expire quietly."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} chars"
    assert "\n" not in text, "excuse must be one line"
    out.write_text(text + "\n", encoding="utf-8")
    print(f"{text} ({len(text)} chars)")


if __name__ == "__main__":
    main()
