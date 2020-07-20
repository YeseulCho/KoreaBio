#! /usr/bin/env python

import sys

if len(sys.argv) != 2 :
    print(f"#usage : python {sys.argv[0]} [txt]")
    sys.exit()

f = sys.argv[1] # result.txt

## 예외처리
# 파일 전체를 한번에 읽어오기
try : 
    with open(f, 'r') as handle :
        read = handle.readlines() # list로 반환
        # ['A : 8954\n', 'C : 5492\n', 'G : 5863\n', 'T : 9594\n']

# file 없을시에 제시 
except FileNotFoundError :
    print(f"{f} not found.. please check..")    
    sys.exit()

print(read)

"""
나가서
python 019.py result.txt 로 입력하면 결과는 아래와 같이 나옴
 # ['A : 8954\n', 'C : 5492\n', 'G : 5863\n', 'T : 9594\n'] 

python 019.py nono.txt 로 입력하면 결과는 아래와 같이 나옴
 # nono.txt not found.. please check..
"""
