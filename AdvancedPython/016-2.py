#! /usr/bin/env python

import sys 

f = sys.argv[1] # print(f)하면 read_sample.txt 로 결과 나타남
d = {}

with open(f, 'r') as handle :
    for line in handle :
        if line.startswith(">") : # > 로 시작하는 행 제거
            continue
        for s in line.strip() : # line에 존재하는 \n strip하고파일 전체  한글자씩 가져오기
            if s in d :
                d[s] += 1
            else :              # d 안에 존재하지 않으면 1이라 지정
                d[s] = 1        # 이렇게 지정해줬기에 그다음 A가 나오면 if문으로 넘어가 +1을 해줄수 있음 

print(d)

"""
python [파일] [인자1] [인자2] ..

나가서
python 016-3.py read_sample.txt 로 입력해주면
read_sample.txt에 A, C, G, T 염기서열이 각각 몇개씩 있는지
dictionary 형태로 알수있다
"""
