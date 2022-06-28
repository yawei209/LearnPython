# -*- coding: utf-8 -*-
# @Time : 2022/6/13 16:36
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : 3.1切片.py
# @Software: PyCharm


L = ['Micheal', 'Sarah', 'Tracy', 'Bob', 'Jack']
# L = ('Micheal', 'Sarah', 'Tracy', 'Bob', 'Jack')
print(L)
#打印L的前三个

r = []
for i in range(3):
    r.append(L[i])
print(r)


#切片
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-1])
print(L[-3:-1])
print(L[-3:])


list = list(range(100))
print(list)
print(list[:10])
print(list[-10:])
print(list[10:20])
print(list[0:10:2])


str = 'ABCDEF'
print(str[:3])
print(str[::2])




def  trim(s):
    while s[:1] == ' ':  #使用while循环，保证多次循环去空格。如果使用if，则只会匹配一次循环去空格
        s=s[1:]         #获取除了s[0]的值，并赋给s
    while s[-1:] == ' ':
        s=s[:-1]        #获取除了s[-1]的值，并赋给s
    return s




# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')