"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the word a grandma
would text about AI.

The word is "knowitall": warm, a little baffled, and funny in one
word — the machine that knows everything, as a grandma would sum
it up to her grandchild. No sentence, no explanation, no
punctuation tricks. One word, nine characters.
"""

import os

WORD = "knowitall"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(WORD)
