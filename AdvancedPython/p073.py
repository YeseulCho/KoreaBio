#! /usr/bin/env python 

cnt = 0
"""
with open("070.vcf", 'r') as handle :
    for line in handle :
        if line.startswith("##") : # ##으로 시작하는 내용 빼기
            continue
        if line.startswith("#") : # header만 가져오기
            header = line.strip().split("\t")
            alt_idx = header.index("ALT")

        splitted = line.strip().split("\t")

        if splitted[alt_idx] == "," :
            cnt += len(splitted[alt_idx].split(","))

        else :
            cnt += 1

print(cnt)
"""


with open("070.vcf", 'r') as handle :
    for line in handle :
        if line.startswith("#") : # header만 가져오기
            continue

        splitted = line.strip().split("\t")
        chrom = splitted[0]
        pos = splitted[1] 
        id_ = splitted[2] 
        ref = splitted[3] 
        alts = splitted[4].split(",") 
                # len으로해도 상관없지만 나중에 하나하나 사용할 경우를 대비해 
        for alt in alts : # ,가 없는 컬럼이라도 그대로 출력됨
            cnt += 1
print(cnt)

