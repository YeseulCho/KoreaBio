#! /usr/bin/env python 

class C :
    def __init__(self) :
        print("calss C의 인스턴스가 생성됨")
        self.name = "ccc"
        self.age = 0

    def say_hi(self) :
        print("hi")

    def add_age(self, n :int ) :
        self.age += n
