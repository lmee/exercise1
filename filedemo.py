# /usr/local/bin/python3
# --*-- coding: utf-8 --*--
# __Author__ = 'Jieer'

poem = '''There was a young lady named Bright,
Whose speed  was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

print(len(poem))

fout = open('relativity','wt')
fout.write(poem)
fout.close()

fout = open('relativity','wt')
print(poem,file=fout)
fout.close()

try:

    fout = open('relativity','xt')
    size = len(poem)

    offset = 0

    chunk = 100

    while True:
        if offset > size:
            break
        fout.write(poem[offset:offset+chunk])
        offset += chunk

    fout.close()
except FileExistsError:
    print('relativity already exists!.That was a close one.')

fin = open('relativity','rt')

poem = fin.read()

fin.close()

print(len(poem))

poem = ''

fin = open('relativity','rt')
chunk = 100
while True:
    fragmet = fin.read(chunk)
    if not fragmet:
        break
    poem += fragmet

fin.close()
print(len(poem))

poem = ''
fin = open('relativity','rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line

fin.close()
print(len(poem))

poem = ''
#使用迭代器的方式读取文本文件更为简洁.
fin = open('relativity','rt')
for line in fin:
    poem += line
fin.close()

print(len(poem))

fin = open('relativity','rt')
lines = fin.readlines()
fin.close()

for line in lines:
    print(line,end='')

bdata = bytes(range(0,255))

print(len(bdata))

fout = open('bfile','wb')

fout.write(bdata)

fout.close()

fout = open('bfile1','wb')

size = len(bdata)

offset =0
chunk =100

while True:
    if offset > size:
        break

    fout.write(bdata[offset:offset+chunk])
    offset += chunk

fout.close()

fin = open('bfile','rb')
bdata = fin.read()
print(len(bdata))
fin.close()
#使用with自动关闭文件
with open('bfile','rb') as fin:
    print(fin.read())

fin = open('bfile','rb')
print(fin.tell())

print(fin.seek(200))

bdata = fin.read()
print(len(bdata))

print(bdata[0])
fin.close()

fin = open('bfile','rb')

print(fin.seek(-1,2))

print(fin.tell())

bdata = fin.read()

print(len(bdata))

print(bdata[0])

import csv
villains = [
    ['Doctor','No'],
    ['Roas','kiebb'],
    ['Mister','Big'],
    ['Auric','Goldfinger'],
    ['Ernst','Blofeld'],
]

with open('villains','wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

with open('villains','rt') as fin:
    cin = csv.reader(fin)
    villains1 = [row for row in cin]

print(villains1)

import xml.etree.ElementTree as et

tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
print(root.tag)

for child in root:
    print('tag:',child.tag,'attributes:',child.attrib,'value:',child.text)
    for grandchild in child:
        print('\ttag:',grandchild.tag,'attributes:',grandchild.attrib,'value:',grandchild)

import datetime

now = datetime.datetime.utcnow()

print(now)


import pickle

now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)

print(now1)

print(now2)

class Tiny():
    def __str__(self):
        return 'tiny'

obj1 = Tiny()

pickled = pickle.dumps(obj1)
print(pickled)
obj2 = pickle.loads(pickled)

print(obj2)

import random

print(random.randrange(2,19))

print(random.choice('Jieer'))