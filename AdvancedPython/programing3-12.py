#! /usr/bin/env python

# 1.

import sys
import json

f = sys.argv[1]

def count_fasta(file_name) :
    d = {}
    with open(file_name, 'r') as handle : 
        for line in handle :
            if line.startswith(">") :
                continue
            for s in line.strip() :
                if s in d :
                    d[s] += 1
                else :
                    d[s] = 1
        return d

d_result = count_fasta(f)
print(d_result)

# 2. 

# 파일 쓰기 
def to_json(l, file_name) :
    with open(file_name, 'w') as handle :
        json.dump(l, handle, indent = 4)

# read_list(d_result)
to_json(d_result, "programing3_result2.json")

