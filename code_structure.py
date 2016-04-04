# /usr/local/bin/python3
# -*- coding: utf-8 -*-
# __Author__ = 'Jieer'

alphabet = 'abcdefg' + \
    'hijklmnop' + \
    'qrstuv'+\
    'wxyz'
print(alphabet)

disaster = True

if disaster:
    print('Woe!')
else:
    print('Whee!')

color = 'puce'

if color == 'red':
    print("'it's a tomato!")
elif color == 'green':
    print("it's a green pepper")
elif color == 'bee purple':
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color-->",color)



x = 7

print(5<x and x<10)

print(5<x<10)

print(5<x or x <10)

#以下几种情况皆会被识别为false,剩余皆为true.

print(False)
print(bool(None))
print(bool(0))
print(bool(0.0))

print(bool(""))
print(bool([]))

print(bool(()))
print(bool({}))
print(bool(set()))

english = 'Monday','Tuesday','wednesday'
french = 'lundi','Mardi','Mercredi'

print(type(english))
print(list(zip(english,french)))
print(dict(zip(english,french)))
print(set(range(1,5)))

number_list = [number - 1 for number in range(1,6)]

print(number_list)

a_list = [number for number in range(1,6) if number % 2 == 1]

print(a_list)

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]

for cell in cells:
    print(cell)

word = 'letters'

letter_counts = {letter: word.count(letter) for letter in set(word)}

print(letter_counts)