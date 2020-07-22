#! /usr/bin/env python

# k-mer generation

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

mer7 = mer(l_seq1, l_seq2, 7)

# print(mer7)

# palindrome

pal_count = 0

for i in mer7 :
    if i == i[::-1] :
        pal_count += 1

print(pal_count)
