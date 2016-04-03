# /usr/local/bin/python3
# -*- coding: utf-8 -*-
# __author__ = 'Jieer'
#__version__ = '1.0'


empty_list = []
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
another_empty_list = list()

print(len(weekdays))

print(list('Jieer'))

a_tuple = ('ready','aim','fire')

list_tuple = list(a_tuple)

print(list(list_tuple))

print(tuple(list_tuple))

birthday = '1985/08/26'

print(birthday.split('/'))

print(weekdays[-2])

print(a_tuple[-1])

print(weekdays[::-1])

# weekdays += list_tuple # Stitching list
weekdays += a_tuple

# weekdays.extend(list_tuple)
# weekdays.extend(a_tuple)

#使用extend() 或者 '+=' 都是可以拼接list,不管后面的元素是list还是tuple,最终得到的结果将是一个拼接后的新list.
#weekdays.append(list_tuple)

print(weekdays)

weekdays.insert(17,'Sunday')
print(weekdays)

del weekdays[-1]

#weekdays.remove('Monday')

print(weekdays.index("Monday"))

print(weekdays * 2)

print('*'.join(weekdays))

print('Fridays' not in weekdays)

#使用sorted()会重新生成一个list的副本,并不会改变当前的list
sorted_list = sorted(weekdays)
#但是使用list的sort()方法,则会改变当前list.
weekdays.sort()
print(sorted_list)

print(weekdays)

a = [1,2,3]

#通过以下三种方式均可以复制一个list

b = a.copy()

c = list(a)

d = a[:]

c.append(4)

print(a)

print(c)

print(d)

#==================================================

#必须是双值序列才可以被转换为dictionary.
lot = [('a','b'),('c','d'),('e','f')]
print(dict(lot))

tol = (['a','b'],['c','d'],['e','f'])
print(dict(tol))

los = ['bz','cd','ef']

tos = ('ab','cd','ef')

print(dict(tos))

print(dict(los))

#使用 update()可以合并字典

pythons = {'Chapman':'Graham','Cleese':'John','Gilliam':'Terry','Idle':'Eric','Jones':'Terry','Palin':'Michael'}

others = {'Marx':'Groucho','Howard':'Moe'}

pythons.update(others)

print(pythons)

del pythons['Marx']

print(pythons)

# pythons.clear()
#
# print(pythons)

print('Chapman' in pythons)

print(pythons.values())

print(pythons.keys())

print(pythons.items())

print(set('Jieer'))

friuts = {'apple':'red','orange':'orange','cherry':'red'}

print(set(friuts))