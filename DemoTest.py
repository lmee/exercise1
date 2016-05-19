ll = [1,2,3,4,5]

print(max(ll))

str1 = 'https://github.com/ZhangBohan/fun_crawler/2245/5.jpg'
lists = str1.split("/")
print('_'.join(lists[-2:]))
for s in str1.split('/'):
    print(s)


alist = [1,2,3,'',0,None]

for s in filter(lambda x:x,alist):
    print(s)
#print(filter(lambda x:x,alist))