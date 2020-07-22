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
        comp += d_comp[s] # dictionary의 key에대한 value값을 comp에 str으로 넣어주기
    return comp

# 외부 파일에서 import 했을때 나타나지 않게 하고싶을때 밑에 if 구문 사용 
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
예를 들어, 
파이썬 파일 028.py를 다른 파일test.py에서 임포트 했을때
p028.comp1("ATGTTATAG") 로 입력하면 
python test.py로 입력햇을때 결과값이 나오게됨  

하지만,
외부에서 실행했을 때 실행되는 것은 함수 
if 안에 있는 것은 실행되지 않도록 한다 
"""

"""
나가서 
python 028.py ATGTTATAG 로 입력
"""
