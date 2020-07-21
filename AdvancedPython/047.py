#! /usr/bin/env python

import tool

t = tool.FASTA("059.fasta")
print(t)
print()

print(dir(t))
print()

print(t.count_base())
print()

print(t.count)
print()

print(len(t))
print()
