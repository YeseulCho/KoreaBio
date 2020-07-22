#! /usr/bin/env python 

cnt = 0
"""
with open("070.vcf", 'r') as handle :
    for line in handle :
        if line.startswith("#") : # #으로 시작하는 내용 빼기 
            continue
        splitted = line.strip().split("\t") 

        if splitted[6] == "PASS" : # PASS가 들어있는 컬럼이 어디인지 알고잇을때 사용
            cnt += 1

print(cnt)
   """

with open("070.vcf", 'r') as handle :
    for line in handle :
        if line.startswith("##") : # ##으로 시작하는 내용 빼기 
            continue
        if line.startswith("#") : # header만 가져오기
            header = line.strip().split("\t")
            filt_idx = header.index("FILTER") # FILTER 컬럼만 가져오기

        splitted = line.strip().split("\t") 

        if splitted[filt_idx] == "PASS" : # FILTER 컬럼의 PASS가 들어있는 행 추출
            cnt += 1

print(cnt)

