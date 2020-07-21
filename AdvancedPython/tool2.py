#! /usr/bin/env python

import sys

class FASTQ :
    
    def __init__(self, file_name) :
        self.file_name = file_name
        self.countQ = 0
        
    def read_count(self) :
        with open(self.file_name, 'r') as handle :
            for line in handle :
                if "@" in line :
                    self.countQ += 1
                else :
                    self.countQ = 1
                    
if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print(f"#usage : python {sys.argv[0]} [fastq]")
        sys.exit()
    file_name = sys.argv[1]
    t = FASTQ(file_name) # 객체 생성
    t.read_count() 
    print(t.countQ)
