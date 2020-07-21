#! /usr/bin/env python

class FASTA :
    def __init__(self, file_name : str) :
        self.file_name = file_name
        self.count = {}

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



