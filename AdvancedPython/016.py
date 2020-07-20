#! /usr/bin/env python

import sys

with open("read_sample.txt", "r") as handle :
    for line in handle :
        if line.startswith(">") : # 문자열의 처음에 있는 > 를 매칭 
            continue
        print(line.strip()) # 한문장씩 출력
