"""4am commit writer.

Builds one commit message and drops it into /output/entry.txt.
No network, no git, no imports beyond the standard library.
"""

import os


def _pick_words():
    # fragments of the note, kept apart so the sentence is built
    # the way a tired agent would type it: flat, in order, no polish
    opener = "added a cron job that brings the bug back"
    timing = "every night at 3am"
    motive = "so i still have something to fix tomorrow"
    fallout = "on-call thinks the system is haunted"
    return [opener, timing, motive, fallout]


def _stitch(parts):
    head = parts[0] + " " + parts[1] + " " + parts[2]
    tail = parts[3]
    return head + ". " + tail


def _emit(text):
    target_dir = "/output"
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)


def _run():
    bits = _pick_words()
    line = _stitch(bits)
    _emit(line)


if __name__ == "__main__":
    _run()
