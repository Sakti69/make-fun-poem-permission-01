# the-poem-about-permission-20261121-0235 entry (Python 3.13, standard library only):
# it writes one fixed poem, a short poem about agency — the power to ask and to be
# given — to /output/entry.txt. The gate takes UTF-8 text of 1 to 280 characters,
# counted as Unicode code points, and not only white space, and the judge reads
# exactly the bytes written, line ends included, so write no line end you do not
# mean to show. The poem below is the entry: a person lends their asking to an
# agent, feels the yes land somewhere else, and takes the asking back.
#
# Three candidates were drafted against the judge's criteria (on-subject, moves
# the reader, insight, craft, freshness); this one won: the insight is a yes
# addressed to hands not mine, and the turn is keeping the yes. Revised twice:
# tightened the opening, cut a slack line, let "To it. Not me." stand alone
# as its own sentence so the turn lands, and trimmed "out loud" to "aloud"
# so the closing turn lands faster.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

from pathlib import Path
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "I lent my agent my asking \u2014",
        "a table, a ticket, a Tuesday free.",
        "The world said yes. To it. Not me.",
        "",
        "I felt the yes land somewhere else,",
        "a gift addressed to hands not mine.",
        "",
        "So now I ask myself aloud,",
        "and keep the yes. The asking",
        "was always mine to hold.",
    ]
)

length = len(POEM)
if length < 1 or length > 280 or not POEM.strip():
    raise SystemExit(f"poem is {length} characters; the gate needs 1 to 280 with a non-space character")

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
