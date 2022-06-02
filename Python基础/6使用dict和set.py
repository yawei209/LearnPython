# -*- coding: utf-8 -*-
# @Time : 2022/6/2 17:07
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : 6使用dict和set.py
# @Software: PyCharm

d = {'Micheal':95, 'Bob': 75, 'Tracy':85}
print(d['Micheal'])


d['Adam'] = 67
print(d)

print(d.get('Micheala', -1))