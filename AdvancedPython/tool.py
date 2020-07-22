#! /usr/bin/env python

import sys

class FASTA :
    def __init__(self, file_name : str) :
        self.file_name = file_name
        self.count = {}
        self.length = 0

    def count_base(self) :
        with open(self.file_name, 'r') as handle :
            for line in handle :                
                if line.startswith(">") :
                    continue
                line = line.strip()
                for s in line :
                    if s in self.count :
                        self.count[s] += 1
                    else :
                        self.count[s] = 1

    def __len__(self) :
        for k, v in self.count.items() :
            self.length += v
        return self.length

class FASTQ : 
    def __init__(self, file_name) :
        self.file_name = file_name
        self.read_num = 0

    def count_read_num(self) :
        cnt = 0
        with open(self.file_name, 'r') as handle :
            for line in handle :
            # count해서 /4할때 나머지가 뭐가 남는지
                # header
                if cnt % 4 == 0 :
                    header = line.strip()
                    self.read_num += 1
                elif cnt % 4 == 1 :
                    seq = line.strip()
                elif cnt % 4 == 3 :
                    qual = line.strip()
                cnt += 1

class BED :
    def __init__(self, file_name) :
        self.file_name = file_name
        chr_num = 0

    def count_chr_num(self) :
        with open(self.file_name, 'r') as handle :
            for lin in handle :
                if line.startswith("#") :
                    continue
                    self.chr_num += 1


if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print(f"#usage : python {sys.argv[0]} [fasta]")
        sys.exit()
    file_name = sys.argv[1]

# FASTA
#    t = FASTA(file_name) # 객체 생성
#    t.count_base() # count_base 실행/ 실행되면 count라는 dic 안에 누적이 될것
#    print(t.count)
#    print(len(t))

# FASTQ
#    t = FASTQ(file_name)
#    t.count_read_num()
#    print(t.read_num)

# BED
 t = BED(file_name)
 t.count_chr_num()
 print(t.chr_num)

"""
python tool.py 059.fasta

python tool.py 061.fastq
"""



