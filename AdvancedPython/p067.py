#! /usr/bin/env python

# k-mer generation

import sys

l_seq1 = ["A", "C", "G", "T"]
l_seq2 = ["A", "C", "G", "T"]

def mer(l_seq1, l_seq2, n) :
    if n == 1 :
        return l_seq2

    else :

        l_result = []

        for i in l_seq1 :
            for j in l_seq2 :
                l_result.append(i + j)

        return mer(l_seq1, l_result, n-1)

n = int(sys.argv[1])
print(mer(l_seq1, l_seq2, n))
