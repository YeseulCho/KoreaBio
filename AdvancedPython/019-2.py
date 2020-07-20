#! /usr/bin/env python

import sys

"""
# Version 1

if len(sys.argv) != 2 :
    print("#usage : python {sys.argv[0]} [txt]")
    sys.exit()

num = int(sys.argv[1])

try :
    print(10 / num)

except ZeroDivisionError :
    print("Zero don't divide it")
"""
"""
# Version 2

if len(sys.argv) != 2 :
    print("#usage : python {sys.argv[0]} [txt]")
    sys.exit()

try : 
    num = int(sys.argv[1])

except ValueError :
    print("input not valid")
    sys.exit()

try :
    print(10 / num)

except ZeroDivisionError :
    print("Zero don't divide it")
    sys.exit()
"""

# Version 3

if len(sys.argv) != 2 :
    print(f"#usage : python {sys.argv[0]} [num]")
    sys.exit()

try :
    num = int(sys.argv[1])
    print(10 / num)

except ValueError :
    print("iniput not valid")
    sys.exit()

except ZeroDivisionError :
    print("Zero don't divide it")
    sys.exit()


"""
나가서
python 019-2.py 2 로 입력하면 결과는
 # 5.0

python 019-2.py 0 으로 입력하면 결과는
 # Zero don't divide it
"""
