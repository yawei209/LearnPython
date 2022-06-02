# -*- coding: utf-8 -*-
# @Time : 2022/6/2 16:32
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : 5循环.py
# @Software: PyCharm

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = 0
#
# for i in l:
#     sum = sum + i
#
# print(sum)
#
#
# sum = 0
# for i in range(11):
#     sum = sum + i
# print(sum)


sum = 0
n = 100
while n > 0:
    sum = sum + n
    n  = n -1
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n  = n -2
print(sum)

sum = 0
n = 100
while n > 0:
    sum = sum + n
    n  = n -2
print(sum)