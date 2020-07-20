#! /usr/bin/env python

import sys

# 오류나지 않도록 
if len(sys.argv) != 2 : # just checks whether you entered at least two elements
    print(f"#usage : python {sys.argv[0]} [fasta]")
        # if 조건에 해당하지 않으면 "#usage : python 파일명[fasta]"라고  제시됨 
    sys.exit()

f = sys.argv[1]
d = {}

# 파일안에 있는 A, C, T, G의 개수 읽어들이기
with open(f, 'r') as handle :
    for line in handle :
        if line.startswith(">") :
            continue
        for s in line.strip() :
            if s in d :
                d[s] += 1
            else :
                d[s] = 1

# 결과 : dictionary 형태 어떻게 만들어졌는지 확인
print(d)


# 전체 개수 알아보기
total = 0
for k, v in d.items() :
    total += v

# 결과 : 전체합한 값 확인
print(total)


# covid dic 나온거 result.txt에 저장하기 
with open("result.txt", 'w') as handle :
    handle.write(f"A : {d['A']}\n")
    handle.write(f"C : {d['C']}\n")
    handle.write(f"G : {d['G']}\n")
    handle.write(f"T : {d['T']}\n")



"""
나가서 
python 016-3.py convid19.fasta 로 입력해서 결과 알아보기

저장한 결과 result.txt 알아보고 싶으면
cat result.txt 로 입력
"""

