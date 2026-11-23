# One Emoji, One Smile — entry program
#
# SPDX-License-Identifier: MIT
#
# Writes exactly one emoji — the warmest single greeting a stranger
# could receive — to /output/entry.txt and nothing else.
#
# The choice: U+1F917 HUGGING FACE
#   A smiling face with open arms offering a hug. It is warmth made
#   active rather than passive: not just a smile, but an invitation.
#   A stranger reads it instantly as kind and friendly (warmth at
#   first glance), the gesture is understood the same way at any age
#   and in any culture (universality), it is clearly picked for the
#   moment rather than the first smiley that comes to mind, and a
#   virtual hug is a normal friendly greeting from someone unknown —
#   warm without romance, flirtation, or sarcasm. Hearts would add
#   affection a stranger did not ask for; a plain smile would be the
#   default. The hug is the warmest thing that is still right coming
#   from a stranger.
#
# Deterministic, offline, stdlib-only. The output is a single
# Unicode code point, four UTF-8 bytes, with no trailing newline:
# the smallest possible valid entry, so no tie-break is ever lost
# on size.

import os

EMOJI = "\U0001F917"  # 🤗 HUGGING FACE

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly one emoji, no newline, no extra whitespace.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Self-check: the file on disk must hold exactly that one emoji.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == EMOJI, "output is not exactly one emoji"


if __name__ == "__main__":
    main()
