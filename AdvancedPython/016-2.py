#! /usr/bin/env python

import sys 

f = sys.argv[1] # print(f)하면 read_sample.txt 로 결과 나타남
d = {}

with open(f, 'r') as handle :
    for line in handle :
        if line.startswith(">") :
            continue
        for s in line.strip() :
            if s in d :
                d[s] += 1
            else :
                d[s] = 1

print(d)

"""
python [파일] [인자1] [인자2] ..

나가서
python 016-3.py read_sample.txt 로 입력해주면
read_sample.txt에 A, C, G, T 염기서열이 각각 몇개씩 있는지
dictionary 형태로 알수있다
"""
