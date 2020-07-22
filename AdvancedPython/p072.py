#! /usr/bin/env python

with open("070.vcf", 'r') as handle :
    for line in handle :
        if line.startswith("##") : # ##으로 시작하는 내용 빼기
            continue
        if line.startswith("#") : # header만 가져오기
            header = line.strip().split("\t")
            id_idx = header.index("ID")
            continue

        splitted = line.strip().split("\t")
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alt = splitted[4]
        if splitted[id_idx] != "." :
            print(f"{chrom}-{pos}-{ref}-{alt}-{id_}")


