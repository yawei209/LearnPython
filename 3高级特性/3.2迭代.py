# -*- coding: utf-8 -*-
# @Time : 2022/6/15 20:16
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : 3.2迭代.py
# @Software: PyCharm


d = {'a':1, 'b':2, 'c':3}
for key,value in d.items():
    print(key,":",value)

for ch in 'ABC':
    print(ch)

def findMinAndMac(L):
    if L ==[]:
        return (None, None)
