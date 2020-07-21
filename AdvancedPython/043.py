#! /usr/bin/env python

import os

print(os.system("ls"))
print()

print(os.system("cat read_sample.json")) # 끝에 0이 붙은 것을 볼 수 있따
print()

a = os.system("cat read_sample.json") # 끝에 0이 붙은 것을 볼 수 있따
print(a)
print()

# 리턴 되는 값이 0인지 아닌지에 따라 return값 확인
print(os.system("ls noname.gz"))
print()

s = os.system("ls noname.gz")
print(s)
print()

# ls의 결과가 문자열로 받아짐
import subprocess
s = subprocess.getoutput("ls")
print(s)
print()

print(s.split())
