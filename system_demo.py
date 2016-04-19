# /usr/local/bin/python3
# --*-- coding:utf-8 --*--
# __Author__ ='Jieer'

fout = open('oops.txt','wt')
print('Oops,I created a file.',file=fout)
fout.close()

import os

print(os.path.exists('oops.txt'))

print(os.path.exists('./oops.txt'))

print(os.path.exists('waffles'))

print(os.path.exists('.'))

print(os.path.exists(".."))

name = 'oops.txt'

print(os.path.isfile(name))

print(os.path.isdir('.'))

print(os.path.isabs(name))

print(os.path.isabs('/big/fake/name'))

print(os.path.isabs('big/fake/name/without/a/leading/slash'))


import shutil

shutil.copy('oops.txt','ohno.txt')

#os.rename('ohwell.txt','oops.txt')

# os.chmod('oops.txt',0o400)

import stat

# os.chmod('oops.txt',stat.S_IRUSR)

# print(os.path.abspath('oops.txt'))
#
# # os.mkdir('poem')
#
# print(os.path.exists('poem'))
#
# os.rmdir('poem')
#
# print(os.path.exists('poem'))

# os.mkdir('poems')
#
# print(os.listdir('poems'))

# os.mkdir('poems/mcintyre')
# print(os.listdir('poems'))

# fout = open('poems/mcintyre/the_good_man','wt')
#
# fout.write('''Cheerful and happy was his mood,
# He to the poor was kind and good,
# Also supplies of coal and wood,
# He never spake a word was rude,
# And cheer'd those did o'er sorrows brood,
# He passed away not understood,
# Because no poet in his praise,
# Had penned a sonnet in his praise,
# 'Tis asd, but such is world's ways.
# ''')
# fout.close
#
# print(os.listdir('poems/mcintyre'))

os.chdir('poems')
print(os.listdir('.'))

import glob

print(glob.glob('m*'))

print(glob.glob('??'))

print(glob.glob('m??????e'))

print(glob.glob('[klm]*e'))