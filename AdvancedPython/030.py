#! /usr/bin/env python 

"""
# Version 1.

Seq1 = "AGTTTATAG"

for i in range(len(Seq1)) :
    if Seq1[i] == "T" and Seq1[i+1] == "T" :
        print(i)
"""

# Version 2

import sys

Seq1 = sys.argv[1]

for i in range(0, len(Seq1), 1) : 
    if Seq1[i:i+2] == "TT" :
        print(i, Seq1[i:i+2])

"""
나가서 
python 030.py AGTTTATAG 입력
"""
