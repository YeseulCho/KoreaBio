#! /usr/bin/env python 

#import pandas as pd
#from matplotlib import pyplot as plt

d = {"snp":0, "ins":0, "del":0}

with open("070.vcf", 'r') as handle :
    for line in handle :
        if line.startswith("#") : # header만 가져오기
            continue

        splitted = line.strip().split("\t")
        alts = splitted[4].split(",") 

        for alt in alts :
            if len(ref) == len(alt) : # snp
                d["snp"] += 1
            elif len(ref) > lne(alt) : # deletion
                d["del"] += 1
            elif len(ref) < len(alt) : # insertion
                d["ins"] += 1
            else : # 방어적 코딩
                raise

print(d)
#df = pd.DataFrame([d])
print(df)
#df.plot.bar() # 그래프
#plt.savefig("v.png") # 그래프 제목
