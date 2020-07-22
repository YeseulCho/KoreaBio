#! /usr/bin/env python

import Bio

from Bio import SeqIO

record = SeqIO.read("059.fasta", "fasta") 

header = record.description
A = record.seq.count("A") # record.seq 문자열과 같은 기능을 하기에 count가 먹힘 
C = record.seq.count("C") # header가 자동적으로 제외됨 
G = record.seq.count("G")
T = record.seq.count("T")

print(f"header : {header}")
print(f"A : {A}") 
print(f"C : {C}") 
print(f"G : {G}") 
print(f"T : {T}") 
