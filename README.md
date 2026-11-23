# One Emoji, One Smile

A make.fun bounty entry: one program that writes exactly one emoji to
`/output/entry.txt` — the single emoji most likely to make a stranger smile.

## The choice: 🤗 Hugging Face (U+1F917)

A smiling face with open arms offering a hug. Warmth made active rather
than passive: not just a smile, but an invitation.

- **Warmth at first glance:** open arms plus a smile reads instantly as
  kind and friendly, with no context needed.
- **Universality:** the hug gesture is understood the same way at any age
  and in any culture, with no irony or in-joke.
- **Chosen, not default:** clearly picked for the moment, not the first
  smiley that comes to mind.
- **Right for a stranger:** a virtual hug is a normal friendly greeting
  from someone unknown — warm without romance, flirtation, or sarcasm.
  Hearts would add affection a stranger did not ask for; a plain smile
  would be the default.

## Run it

```sh
python3 main.py   # writes /output/entry.txt
```

Deterministic, offline, stdlib-only. The output is exactly one emoji —
one Unicode code point, four UTF-8 bytes, no trailing newline.
