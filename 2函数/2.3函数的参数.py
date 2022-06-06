# -*- coding: utf-8 -*-
# @Time : 2022/6/2 20:03
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : 2.3函数的参数.py
# @Software: PyCharm

def power(x, n=2):
    s = 1
    while n >0:
        n = n -1
        s = s * x
    return s
# print(power(2))


# def enroll(name, gender):
#     print(name)
#     print(gender)

def enroll(name, gender, age=6, city='Beiging'):
    print('name:', name)
    print('gender:',gender)
    print('age:',age)
    print('city',city)

# enroll('Sarah','Female')
# print('\n')
# enroll('Bob','male',7,'Shanghai')
# print('\n')



#####可变参数:允许传入0个或任意个参数#####
'''
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
'''
def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n*n
    return sum


# print(calc([1, 3, 5]))
# print(calc())
###可变参数需要传入一个tuple 或list
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
calc(*nums)





###关键字参数###
'''
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
'''
def person(name, age, **kw):
    print('name:',name, 'age:',age, 'other:',kw)
person('Micheal',30)
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',job='Engineer')


###或者直接传入一个字典

dic = {'gender':'Famale', 'job':'teacher', 'city':'Zhenzhou'}
person('hui',31,**dic)