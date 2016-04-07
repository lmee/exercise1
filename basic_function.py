# /usr/local/bin/python3
# --*-- coding: utf-8 --*--
# __author__ = 'Jieer'

import sys
import random
import collections
print("System.args",sys.argv)
print(sys.path)

possibilities = ['rain','snow','sleet','frog','sun','who knows']

print(random.choice(possibilities))

peridoic_talbe = {'Hydrogen':1,'Helium':2}
carbon = peridoic_talbe.setdefault('Carbon',12)
print(carbon)

peridoic_talbe = collections.defaultdict(int)

peridoic_talbe['Hydrogen'] = 1

print(peridoic_talbe['Lead'])

print(peridoic_talbe)

bestiary = collections.defaultdict(lambda :'Huh')

print(bestiary['E'])

food_counter = collections.defaultdict(int)

breakfast = ['spam','spam','eggs','spam']

for food in breakfast:
    food_counter[food] +=1

for food,count in food_counter.items():
    print(food,count)

breakfast_counter = collections.Counter(breakfast)
print(breakfast_counter)
print(breakfast_counter.most_common())

quotes = collections.OrderedDict([
    ('Moe','A wise guy,huh?'),
    ('Larry','Ow!'),
    ('Curly','Nyuk nyuk!'),
])

for stooge in quotes:
    print(stooge)
    print(stooge)

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('a'))
print(palindrome('racecar'))

def another_palindrome(word):
    return word == word[::-1]

print(another_palindrome('racecar'))