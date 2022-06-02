# -*- coding: utf-8 -*-
# @Time : 2022/6/2 16:15
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : 条件判断.py
# @Software: PyCharm


# age = int(input('Please input your age:'))
# if age >= 18:
#     print(f'your age is {age}.')
#     print('adult')
# elif age >=16:
#     print(f'your age is {age}.')
#     print('teenager')
# else:
#     print(f'your age is {age}.')
#     print('Kid')


height = 1.83
weight = 86.5
bmi = weight/height**2
print(bmi)

if bmi >= 32:
    print('严重肥胖')
elif bmi >= 28:
    print('肥胖')
elif bmi >=25:
    print('过重')
elif bmi >=18.5:
    print('正常')
else:
    print('过轻')