#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Unidecode provides some awesome unicode removal scrubbing for Alfred.
"""

# Examples:
# echo "curly single (‘’), curly double (“”), fractions (¼ ½ ¾)" | /usr/bin/python main.py

# # https://github.com/avian2/unidecode
# echo "[install]\nprefix=" > setup.cfg
# pip2 install --target=. unidecode
#

from __future__ import absolute_import, division, print_function, unicode_literals
import sys
import codecs
from unidecode import unidecode


def main():
    # Assume UTF-8 input
    UTF8Reader = codecs.getreader('utf8')
    sys.stdin = UTF8Reader(sys.stdin)

    # support piping into this script
    if sys.stdin.isatty():
        input = ""
    else:
        input = "".join(sys.stdin)

    # ASCII-ify the text
    result = unidecode(input)
    print(result)


if __name__ == "__main__":
    main()
