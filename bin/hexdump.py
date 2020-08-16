#!/usr/bin/env python3

"""
usage: hexdump.py [-h] [-C]

show bytes as themselves, don't see them only as terminal control codes and character encodings

optional arguments:
  -h, --help  show this help message and exit
  -C          show hex and us-ascii

bugs:
  show UTF-8 emoji where they appear, unlike Bash "hexdump" holding to "us-ascii" from 1967
  acts like "hexdump -h" if called with no args, unlike Bash "hexdump"

examples:
  Oh no! No examples disclosed!! 💥 💔 💥
"""
# FIXME FIXME: fix "hexdump" bugs: show UTF-8 emoji where they appear


import sys

import argdoc


def main():
    args = argdoc.parse_args()
    sys.stderr.write("{}\n".format(args))
    sys.stderr.write("{}\n".format(argdoc.format_usage().rstrip()))
    sys.stderr.write("hexdump.py: error: not implemented\n")
    sys.exit(2)  # exit 2 from rejecting usage


if __name__ == "__main__":
    main()


# copied from:  git clone https://github.com/pelavarre/pybashish.git
