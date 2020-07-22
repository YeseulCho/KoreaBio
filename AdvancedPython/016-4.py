#! /usr/bin/env python

import sys
import gzip # gzip open에 사용

# covid19 파일 압축후 진행

"""
Q : covid file 압축후 
    압축 파일 읽어서 ACGT의 개수와 전체길이를 result1.txt로 만드는 
    파이썬 스크립트 작성하기
"""

if len(sys.argv) != 2 :
    print(f"#usage ; python {sys.argv[0]} [fasta.gz]")
    sys.exit()

f = sys.argv[1]
d = {}

with gzip.open(f, 'rb') as handle : # rb : read binary
    for line in handle :
        line = line.decode("utf-8").strip() # string으로 바꿔주기 
        
        if line.startswith(">") :
            continue

        # 파일안에 글자들 개수 세기
        for s in line :
            if s in d :
                d[s] += 1
            else :
                d[s] = 1

# 결과 저장
with open("result1.txt", 'w') as handle :
    handle.write(f"A : {d['A']}\n")
    handle.write(f"C : {d['C']}\n")
    handle.write(f"G : {d['G']}\n")
    handle.write(f"T : {d['T']}\n")

