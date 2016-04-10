# /usr/local/bin/python3
# --*-- coding:utf-8 --*--
# __Author__ = 'Jieer'


class Animal:

    def __init__(self,name):
        self.name = name

    def shout(self):
        print(self.name+" is shoutting!!!")


class Duck(Animal):

    def __init__(self,input_name):
        self.__name = input_name

    def shout(self):
        print("Duck is shouting")

    @property
    def name(self):
        print('indside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

   # name = property(get_name,set_name)

a = Animal("a1")
a.shout()

a1 = Duck("a2")
# a1.set_name('Doo Doo')
a1.name = 'Doo Doo'

a1.shout()
# print(a1.get_name())
print(a1.name)

class A:
    count = 0

    def __init__(self):
        A.count += 1

    @staticmethod
    def exclaim():
        print('I m an A!')

    @classmethod
    def kids(cls):
        print('A has', cls.count,'little objects')

# easy_a = A()
#
# breezy_a = A()
#
# wheezy_a = A()

A.kids()
A.exclaim()

class Word():
    def __init__(self,text):
        self.text = text

    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

    def __str__(self):
        return 'Jieer,'+self.text

first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first == second)
print(first == third)
print(second)

from collections import namedtuple

Duck = namedtuple('Duck','bill,tail')

duck = Duck('wide orange','long')

print(duck)

print(duck.bill)

print(duck.tail)