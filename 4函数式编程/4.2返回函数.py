#!/usr/bin/env python
# _*_ coding: utf-8 _*_

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs  #fs 是一个list

f1, f2, f3= count()

print(f1())
print(f2())
print(f3())