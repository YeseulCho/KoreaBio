#! /usr/bin/env python 

import sys

def read_txt(file_name : str) -> str :
    ret = "" # 빈 문자열
    with open(file_name, 'r') as handle : # 파일 불러오기
        for line in handle :
            if line.startswith(">") :
                continue
            ret += line.strip()
        return ret

# tsv 파일 읽기
def read_tsv(file_name : str) -> list :
    ret = []
    with open(file_name, 'r') as handle :
        for line in handle :
            if line.startswith("#") :
                header = line.strip().split(",")
                continue
            splitted = line.strip().split(",")
            # zip 을 사용하면 list들의 순서에 맞게 dict의 형태가 형성됨
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret


if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print("#usage : python {sys.argv[0]} [txt]")
        sys.exit()

    file_name = sys.argv[1] # 첫번째 인자로 가져온걸 file_name으로 넣기
    txt = read_tsv(file_name) # file_name으로 가져온 것을 출력한다
    print(txt)

"""
python 037.py read_sample.csv
"""

