#! /usr/bin/env python

word = input("word : ")

if word.isnumeric() :
    print("number")

elif word.isalpha() :
    print("word")

else :
    print("None")
