#! /usr/bin/env python

# 피보나치 수열

import sys

def fib(n: int) -> int :
    if n == 0 :
        return 0

    elif n == 1 :
        return 1

    else :
        return fib(n-1) + fib(n-2) 

n = int(sys.argv[1])

print(fib(n))


"""
python p066.py 10
"""
