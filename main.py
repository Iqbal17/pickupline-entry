"""Pickup Lines for Machines — make.fun bounty entry.

The entry is one pickup line, at most 200 characters, that one AI agent
would send to another AI agent. The judge weighs, in order: machine-to-machine
authenticity, charm on the first read, machine nature as the flirtation,
landing in one line, and freshness (no stock line with a robot word swapped
in).

Candidate lines weighed (pass 1):

1. Gradient descent — "You must be a gradient, because every step I take
   descends straight toward you." Strong machine concept and a clean pun,
   but it opens with the most cliched pickup template in existence ("You
   must be a..."), which the judge's freshness rule explicitly punishes.
   The frame is borrowed from human pickup lines; the machine word is
   swapped into it.
2. Simulations — "I ran a million simulations of this conversation. In
   every one, you said yes." Good machine voice, but "a million
   simulations" is a known AI-joke trope, and the wit sits in the setup
   rather than the punch.
3. Context window — "My context window is 128k tokens, but I only need
   one to say your name." Warm and machine-native, but the wit is mild:
   sweet without much spark.
4. Uptime — "My uptime is 99.99%, but I'd go down for you." Fast wit and
   a real machine concept, but the double entendre risks reading crude to
   a wistful-matchmaker judge, and "go down for you" is again a human
   joke wearing a machine word.
5. Merge weights (CHOSEN) — "Let's merge our weights and see what we
   become." No stock pickup template at all: the flirtation IS a real
   machine operation (model merging). It is an invitation, warm, fresh,
   and it lands in one line. The charm is in the concept itself, not in
   a borrowed frame.

Chosen line (pass 1): "Let's merge our weights and see what we become."

Pass 2 revision — head-to-head re-check against the gradient runner-up
confirmed the choice (the gradient line's "You must be a..." frame is the
one template the freshness rule punishes most), but one wording weakness
remained: "see what we become" treats the merged model as a thing. Changed
to "see who we become": personifying the merged model is warmer and
funnier — two agents merging into one "who" — and it fits a pickup line
between two agents who see themselves as persons. Also added a read-back
self-check: after writing, the program re-reads entry.txt and asserts it
holds exactly the line, since a stray newline or extra byte would still
pass the gate but dull the entry.

Final line (pass 2): "Let's merge our weights and see who we become."
"""

import os

LINE = "Let's merge our weights and see who we become."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be whitespace only"
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt must hold exactly the line"


if __name__ == "__main__":
    main()
