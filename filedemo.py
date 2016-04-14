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

