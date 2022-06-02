# -*- coding: utf-8 -*-
# @Time : 2022/6/2 14:47
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : 2字符串和变量.py
# @Software: PyCharm

s = 'Hello %s'   %('world')
print(s)

s2 = 'Hi, %s, you have $%d.'      %('Micheal', 1000)
print(s2)

s3 = r'Hi, %s, you have $%d.'      %('Micheal', 1000)
print(s3)

s4 = 'Age: %s. Gender: %s'  %(25, True)
print(s4)

s5 = 'growth rate: %d %%'   %(5)
print(s5)

s6 = '%2d-%02d' %(3,1)
print(s6)

s7 = '%.2f' %(3.1415926)
print(s7)

s8 = 'Hello, {0}, 成绩提升了{1:.1f}%'.format('小明',17.125)
print(s8)


r = 2.5
s = 3.14 * r**2

str = f'The area of a circle with radius {r}cm is {s:.2f}cm2'
print(str)