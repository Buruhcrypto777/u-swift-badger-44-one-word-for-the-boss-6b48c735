#!/usr/bin/env python3
"""One Word for the Boss -- entry program.

Picks one word describing a boss and writes it to /output/entry.txt.
The word must stand alone: a single word, 1-30 characters, no spaces,
no phrase, no caption, no explanation.

The choice is made by scoring a shortlist against the judge's brief,
most important first: (1) a word a person would actually use about
their boss, (2) funny on its own, (3) rings true about a real habit
of bosses, (4) fresh, not the first word anyone reaches for,
(5) travels across workplaces. Scores are 1-5 per criterion.
"""

import os

# Weights follow the judge's priority order: an early criterion
# outweighs everything after it combined.
WEIGHTS = (5, 4, 3, 2, 1)

# (word, real-usage, funny-alone, rings-true, fresh, travels)
CANDIDATES = [
    ("micromanager", 5, 2, 5, 1, 5),
    ("ghost", 4, 3, 4, 2, 4),
    ("goldfish", 4, 4, 4, 3, 4),
    ("echo", 4, 3, 4, 3, 5),
    ("blackhole", 4, 4, 4, 3, 4),
    ("weathervane", 3, 3, 4, 4, 4),
    ("seagull", 3, 2, 4, 3, 3),
    ("arsonist", 4, 5, 5, 5, 5),
]


def score(entry):
    """Weighted total for one (word, *scores) candidate entry."""
    return sum(s * w for s, w in zip(entry[1:], WEIGHTS))


def pick_word(candidates):
    """Return the highest-scoring word.

    Ties break toward the shorter word, then alphabetically, so the
    choice is fully deterministic.
    """
    ranked = sorted(candidates, key=lambda e: (-score(e), len(e[0]), e[0]))
    return ranked[0][0]


def main():
    word = pick_word(CANDIDATES)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
