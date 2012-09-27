#!/usr/bin/env python
# encoding: utf-8
# Author: João S. O. Bueno <jsbueno@simplesconsultoria.com.br>
# License: GPL version 3 or later

"""
This script simply parses file from a PSD Imgae (Adobe Phtooshop native
image format), and printout the resources used in the file tagged
with "/Name" -- most of them are font (typeface) names.

Since GIMP as of 2.8 can't import Photoshop text layers as text, this
script can help designers to see what fonts where used in a given image
without resorting to a Photoshop install.

Tested with Python 2.6, 2.7 and 3.2, pypy 1.8
"""

from __future__ import unicode_literals, print_function
import sys

IDENT = "    "

def parse(data, seq=b"/Name"):
    end = False
    index = -1
    names = set()
    while not end:
        index = data.find(seq, index + 1)
        if index == -1:
            break
        pattern = data[index:index + 500]
        pattern = pattern.split(b"(")[1].split(b")")[0].decode("utf-16")
        if pattern: names.add(pattern)
    return names

def main(filenames):
    for filename in filenames:
        print (filename + ":")
        data = open(filename, "rb").read()
        results = parse(data)
        for result in sorted(results):
             print (IDENT + result)
        print(end="\n")

if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Usage: psd_print_resources.py  <filename.psd> ...", file=sys.stderr)
    main(sys.argv[1:])
