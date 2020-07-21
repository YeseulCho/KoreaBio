#! /usr/bin/env python

import readtxt2

l = readtxt2.read_csv("read_sample.csv")
print(l)

# readtxt2.to_json(l) # 이건 파일이름 안들어가있어서 실행 안됨
print(readtxt2.to_json(l, "result.json"))
