#!/usr/bin/env python
# _*_ coding: utf-8 _*_

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()


run_twice(cat)