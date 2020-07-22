#! /usr/bin/env python

import p062

print(dir(p062))

c = p062.C()

# print(p062.name)

print(c.name)

print(c.say_hi())

# print(c.add_age())

print(c.add_age(5))

print(c.age)

## __str__ __repr__ 사용후

print(c) # __str__ 호출됨

c # __repr__

## __abs__ __len__ 사용후

c = p062.C()

c # __repr__

print(abs(10))

print(abs(-10))

print(abs(c)) # __abs 

print(len("asdf"))

# print(len(c))
print()
# __add__ 사용후

c1 = p062.C()

c2 = p062.C()

c1.age = 10

c2.age = 5

print(c1.age)

print(c2.age)

print(c1.age + c2.age)

print(c1 + c2)




