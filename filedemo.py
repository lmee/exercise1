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



# import sqlite3
#
# conn = sqlite3.connect('enterprise.db')
#
# curs = conn.cursor()

# curs.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY ,
# count INT , damages FLOAT)''')

# curs.execute('INSERT INTO zoo VALUES ("duck",5,0.0)')
#
# curs.execute('INSERT INTO zoo VALUES ("bear",2,1000.0)')
#
# ins = 'INSERT INTO zoo (critter,count,damages) VALUES(?,?,?)'
#
# curs.execute(ins,('weasel',1,2000.0))

# curs.execute('SELECT * FROM zoo')

# curs.execute('SELECT * FROM zoo ORDER BY count ')

# curs.execute('SELECT * FROM zoo ORDER BY count DESC ')

# curs.execute('''SELECT * FROM zoo WHERE
#   damages = (SELECT MAX(damages) FROM zoo)''')
#
# rows = curs.fetchall()
#
# print(rows)
#
# curs.close()
#
# conn.close()

import redis

conn = redis.Redis()

print(conn.keys("*"))

conn.set('secret','ni!')

conn.set('carats',24)

conn.set('fever','101.5')

print(conn.get('secret'))

print(conn.get('carats'))

print(conn.get('fever'))

conn.setnx('secret','icky-icky-icky-ptang-zoop-boing!')

print(conn.get('secret'))

conn.getset('secret','icky-icky-icky-ptang-zoop-boing!')

print(conn.get('secret'))

print(conn.getrange('secret',-6,-1))

print(conn.setrange('secret',0,'ICKY'))

print(conn.get('secret'))

conn.mset({'pie':'cherry','cordial':'sherry'})

print(conn.mget(['fever','carats']))

conn.delete('fever')

conn.lpush('zoo','bear')

conn.lpush('zoo','alligator','duck')

conn.linsert('zoo','before','bear','beaver')
conn.linsert('zoo','after','bear','cassowary')

conn.lset('zoo',2,'marmoset')

conn.lpush('zoo','yak')

print(conn.lindex('zoo',3))

print(conn.lrange('zoo',0,2))

print(conn.ltrim('zoo',1,4))

print(conn.lrange('zoo',0,-1))

conn.hmset('song',{'do':'a deer','re':'about a deer'})

print(conn.hset('song','mi','a note to follow re'))

print(conn.hget('song','mi'))

print(conn.hmget('song','re','do'))

print(conn.hkeys('song'))

print(conn.hvals('song'))

print(conn.hlen('song'))

print(conn.hgetall('song'))

conn.hsetnx('song','fa','a note that rhymes with la')


conn.sadd('soo','duck','goat','turkey')

print(conn.scard('soo'))

print(conn.smembers('soo'))

print(conn.srem('soo','turkey'))

conn.sadd('better_zoo','tiger','wolf','duck')

print(conn.sinter('soo','better_zoo'))

conn.sinterstore('fowl_zoo','soo','better_zoo')

print(conn.smembers('fowl_zoo'))

print(conn.sunion('soo','better_zoo'))

conn.sunionstore('fabulous_zoo','soo','better_zoo')

print(conn.smembers('fabulous_zoo'))

print(conn.sdiff('soo','better_zoo'))

conn.sdiffstore('zoo_sale','soo','better_zoo')

print(conn.smembers('zoo_sale'))

import  time

now = time.time()
print(now)

conn.zadd('logins','smeagol',now)

conn.zadd('logins','sauron',now+(5*60))

conn.zadd('logins','bilbo',now+(2*60*60))

conn.zadd('logins','treebeard',now+(24*60*60))

print(conn.zrank('logins','bilbo'))

print(conn.zscore('logins','bilbo'))

print(conn.zrange('logins',0,-1))

print(conn.zrange('logins',0,-1,withscores=True))


days = ['2013-02-25','2013-02-26','2013-02-27']

big_spender = 1089

tire_kicker = 40459

late_joiner = 550212

conn.setbit(days[0],big_spender,1)

conn.setbit(days[0],tire_kicker,1)


conn.setbit(days[1],big_spender,1)

conn.setbit(days[2],big_spender,1)

conn.setbit(days[2],late_joiner,1)

for day in days:
    print(conn.bitcount(day))


print(conn.getbit(days[1],tire_kicker))

print(conn.bitop('and','everyday',*days))

import time
key = 'now you see it'

conn.set(key,'but not for long')

conn.expire(key,5)

conn.ttl(key)

print(conn.get(key))

time.sleep(6)

print(conn.get(key))