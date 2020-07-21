#! /usr/bin/env python

# 2
#name = input("name : ")
#print(name)


# 3
def base_select(base) :

    if base == "A" :
        print("Adenine")
    elif base == "C" :
        print("Cytosine")
    elif base == "G" :
        print("Guanine")
    elif base == "T" :
        print("Thymine")
    elif base == "U" :
        print("Uracil")

base_select("T")

# 3 - 2 # 다시해보기
#import sys

#Seq1 = sys.argv[1]

#for i in range(len(Seq1)) :
#    if Seq1[i] == "A" :
#        print("Adenine")


# 4
#num = int(input("number : "))

#try :
#    print(10/num)

#except ZeroDivisionError :
#    print("wrong division")

# 4 - 2

#import sys

#num1 = sys.argv[1]

#try :
#    print(10/int(num1))

#except ZeroDivisionError :
#    print("wrong division")


# 4 -3 

def divide(num2) :

    try :
        result = 10/num2
    
    except ZeroDivisionError :
        result = "wrong division"

    return result

print(divide(5))

# 5

def factorial(num) :
    result = 1

    for i in range(1, num+1, 1) :
            result *= i

    return result

print(factorial(5))
