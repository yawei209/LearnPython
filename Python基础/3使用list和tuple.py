# -*- coding: utf-8 -*-
# @Time : 2022/6/2 15:40
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : 3使用list和tuple.py
# @Software: PyCharm


classmates = ['Micheal', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])

classmates.append('Adam')

print(classmates)

classmates.insert(1, 'Jack')
print(classmates)


poped_classmate = classmates.pop()
print(classmates)
print(poped_classmate)

poped_classmate2 = classmates.pop(1)
print(classmates)
print(poped_classmate2)

classmates[1] = 'Sarah'
print(classmates)