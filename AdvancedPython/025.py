#! /usr/bin/env python

"""
Q : 문자열 변수 Seq1에"ATGTTATAG"가 담겨있습니다
    Seq1에서 3칸씩 건너뛰며 출력, 즉 첫번째, 네번째, 일곱번째만
    출력하는 프로그램을 작성해보시오

"""
Seq1 = "ATGTTATAG"

for i in range(0, len(Seq1), 3) :
    # print(i) # 0 3 6 
    print(i, Seq1[i]) # 인덱싱


