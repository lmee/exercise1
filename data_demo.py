# /usr/local/bin/python3
# --*-- coding: utf-8 --*--
# __Author__ = 'Jieer'

# def unicode_test(value):
#     import unicodedata


snowman = '\u2603'

print(len(snowman))

ds = snowman.encode('utf-8')

print(len(ds))

print(ds)

ds = snowman.encode('ascii','ignore')

print(ds)

print(snowman.encode('ascii','replace'))

print(snowman.encode('ascii','backslashreplace'))

print(snowman.encode('ascii','xmlcharrefreplace'))

place = 'caf\u00e9'

print(place)

print(type(place))

place_bytes = place.encode('utf-8')

print(place_bytes)

print(type(place_bytes))

place2 = place_bytes.decode('utf-8')
print(place2)

# place3 = place_bytes.decode('ascii')
# print(place3)

place4 = place_bytes.decode('latin-1')

print(place4)

place5 = place_bytes.decode('windows-1251')

print(place5)

print('%s'%42)

print('%d'%42)

print('%x'%42)

print('%o'%42)

print('%s'%7.03)

print('%f'%7.03)

print('%e'%7.03)

print('%g'%7.03)

actor = 'Richard Gere'

cat = 'Chester'

weight = 28

print("My wife's favorite actor is %s"%actor)

print("Our cat %s weighs %s punds"%(cat,weight))

n = 42

f = 7.03

s = 'string cheese'

print('%d %f %s'%(n,f,s))

print('%10d %10f %10s'%(n,f,s))

print('%-10d %-10f %-10s'%(n,f,s))

print('%10.4d %10.4f %10.4s'%(n,f,s))

print('%.4d %.4f %.4s' %(n,f,s))

print('%*.*d %*.*f %*.*s'%(10,4,n,10,4,f,10,4,f))

print('{} {} {}'.format(n,f,s))

print('{2} {0} {1}'.format(f,s,n))

#新式格式化右对齐">"
print('{0:>10d}{1:>10f}{2:>10s}'.format(n,f,s))

#新式格式化左对齐"<"
print('{0:<10d}{1:<10f}{2:<10s}'.format(n,f,s))

#最小域宽为10,居中
print('{0:^10d}{1:^10f}{2:^10s}'.format(n,f,s))

#如果想要使用空格以外的字符进行填充,只需要把它放在:之后,其余任何排版符(<,>,^)和宽度标识符之前即可.
print('{0:!^20s}'.format('BIG SALE'))

import re

source = 'Young Frankenstein'

m = re.match('Youa',source)

if m:
    print(m.group())

m = re.search('Frank',source)

if m:
    print(m.group())

m = re.match('^You',source)

if m:
    print(m.group())

m = re.match('.*Frank',source)

if m:
    print(m.group())


m = re.search('Frank',source)
if m:
    print(m.group())

m = re.findall('n',source)

print(m)

m = re.findall('n.',source)
print(m)

m = re.findall('n.?',source)
print(m)

m = re.split('n',source)

print(m)

#sub()替换匹配 和字符串replace()方法类似.
m = re.sub('n','?',source)

print(m)

import string

printtalbe = string.printable

print(len(printtalbe))

print(printtalbe[:50])

print(re.findall('\d',printtalbe))

print(re.findall('\D',printtalbe))

print(re.findall('\w',printtalbe))

print(re.findall('\s',printtalbe))

source = '''I wish I ay, I wish I might
        ...Have a dish of fish tonight.'''

print(re.findall('wish',source))

print(re.findall('wish|fish',source))

print(re.findall('^wish',source))

print(re.findall('^I wish',source))

print(re.findall('fish$',source))

print(re.findall('fish tonight.$',source))


print(re.findall('[wf]ish',source))

print(re.findall('[wsh]+',source))

print(re.findall('ght\w',source))

print(re.findall('I(?=wish)',source))

print(re.findall('(?<=I)wish',source))

print(re.findall(r'\bfish',source))

blist = [1,2,3,255]

the_bytes = bytes(blist)

print(the_bytes)

#bytearray 类型的变量是可变的.
the_byte_array = bytearray(blist)

print(the_byte_array)

the_byte_array[1]=127

print(the_byte_array)

the_bytes = bytes(range(0,256))

the_byte_array = bytearray(range(0,256))

print(the_byte_array)

import struct

valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'

if data[:8] == valid_png_header :
    width, height = struct.unpack('>LL',data[16:24])
    print('Valid  PNG, width',weight,'height',height)
else:
    print('Not a valid PNG')

print(struct.pack('>L',154))

