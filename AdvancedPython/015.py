#! /usr/bin/env python

import sys
"""
- sys 라이브러리는 파이썬에서 명령행을 받기위한 라이브러리
- sys.argv 는 배열
- sys.argv[0]에는 기본적으로 python 실행파일의 경로가 담김
  그래서 sys.argv 배열의 길이는 기본적으로 1
"""

print(len(sys.argv)) # 1

print(sys.argv[0]) # ./015.py

print(f"Hello {sys.argv[0]}") # Hello ./015.py

print(f"run -> sample{sys.argv[0]}") # run -> sample./015.py
