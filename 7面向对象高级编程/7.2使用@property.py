#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#1
# class Student(object):
#
#     def get_score(self):
#          return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# s = Student()
# s.set_score(60)
# print(s.get_score())

# s.set_score(999)

#2 @property装饰器就是负责把一个方法变成属性调用的
# class Student(object):
#
#     @property #getter 方法
#     def score(self):
#         return self._score
#
#     @score.setter #setter 方法
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# s = Student()
# s.score = 60
# print(s.score)
# s.score = 999

#3定义只读属性
# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2022 - self._birth
#
# s = Student()
# s.birth = 1991
# print(s.birth)
# print(s.age)
# s.age = 18 #会报错，无法设置成功


#习题 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

s = Screen()
s.width = 6
s.height = 10
print(s.width)
print(s.height)
print(s.resolution)


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')