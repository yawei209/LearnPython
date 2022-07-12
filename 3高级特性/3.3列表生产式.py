#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/7/12 19:17
# @Author : zhangyawei
# @Version：V 0.1
# @File : 3.3列表生产式.py

L1 = list(range(1,11))
print(L1)

L2 = []
def fun():
    for x in range(1,11):
        if x % 2 == 0:
            L2.append(x**2)
fun()
print(L2)

L3 = [x*x for x in range(1, 11) if x % 2 ==0 ]
print(L3)

L4 = [m+n for m in 'ABC' for n in 'XYZ']
print(L4)


L5 = []
def fun2():
    for m in 'ABC':
        for n in 'XYZ':
            L5.append(m + n)
fun2()
print(L5)


d = {'x':'A', 'y':'B', 'z':'C'}

for k, v in d.items():
    print(k,'=',v)

L6 = [k + '=' + v for k, v in d.items()]
print(L6)


L7 = ['Hello', 'World', 'IBM', 'Apple']
L8 = [s.lower() for s in L7]
print(L8)



L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')