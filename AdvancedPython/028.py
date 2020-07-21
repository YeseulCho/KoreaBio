#! /usr/bin/env python

"""
Q : Seq1 = "ATGTTATAG"
    A는 T, G는 C, C는 G, T는 A로 바꾸어 출력
"""
"""
Seq1 = "ATGTTATAG"

Seq1 = Seq1.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g").upper()

print(Seq1)
"""

"""
강사님 ver.
"""

import sys

# Version 1
def comp1(seq : str) -> str: # string인거 명시적으로 보여주기
    comp = ""
    for s in seq :
        if s == "A" :
            comp += "T"
        elif s == "C" :
            comp += "G"
        elif s == "G" :
            comp += "C"
        elif s == "T" :
            comp += "A"
    return comp

# Version 2
def comp2(seq : str) -> str : 
    d_comp = {"A":"T", "T":"A", "C":"G", "G":"C"} # 상보적 dic 만들어주기
    comp = ""
    for s in seq :
        comp += d_comp[s]
    return comp

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print(f"#usage : python {sys.argv[0]} [string]")
        sys.exit()

seq = sys.argv[1] # ATGTTATAG
c1 = comp1(seq)
c2 = comp2(seq)
print(seq)
print()
print(c1)
print()
print(c2)


"""
나가서 
python 028.py ATGTTATAG 로 입력
"""
