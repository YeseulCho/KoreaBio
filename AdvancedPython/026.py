#! /usr/bin/env python

"""
Seq1 = "ATGTTATAG"
Seq1에서 3칸씩 건너뛰며 출력하기

ATG
TTA
TAG
"""

Seq1 = "ATGTTATAG"

for i in range(0, len(Seq1), 3) :
    print(Seq1[i:i+3]) # 슬라이싱 # triple codon 만든것

    # 이후에 dictionary에 아미노산 지정
