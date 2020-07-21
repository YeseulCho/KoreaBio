#! /usr/bin/env python

l_num = [3, 1, 1, 2, 0, 0, 2, 3, 3]

for i in range(len(l_num)) :
    for j in range(len(l_num)) :
        if l_num[i] >= l_num[j] :
            print("Max :", l_num[i])
        elif l_num[i] <= l_num[j] :
            print("Min : ", l_num[i])
"""


max_val = l_num[0] # list의 처음 값으로 max, min으로 지정
min_val = l_num[0]

for elem in l_num :
    if elem > max_val :
        max_val = elem
    if elem < min_val :
        min_val = elem

print(f"max : {max_val}") # 3
print(f"min : {min_val}") # 0
"""
