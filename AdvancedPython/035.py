#! /usr/bin/env python

import sys

"""

"""
"""
with open("read_sample.txt", 'r') as sample :
    for line in sample :

        if line.startswith(">") :
            continue

        for s in line :
            print(s("\n"))

"""
def read_txt(file_name : str) -> str : # 가시적
    ret = "" # 빈 문자열
    with open(file_name, 'r') as handle : # 파일 불러오기
        for line in handle :
            if line.startswith(">") : # >header 제외 
                continue
            ret += line.strip() # 빈문자열에 라인 추가하는 방식
    return ret

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print("#usage : python {sys.argv[0]} [txt]")
        sys.exit()

    file_name = sys.argv[1] # 첫번째 인자로 가져온걸 file_name으로 넣기 
    txt = read_txt(file_name) # file_name으로 가져온 것을 출력한다 
    print(txt)

"""
python read_txt.py read_sample.txt
"""
