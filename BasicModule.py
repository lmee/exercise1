# /usr/bin/python3

print("This is a script file,it's will upload to github, so cool!")
todos = 'get,gloves,get mask,give cat vitamins,call ambulance'
todos_list=todos.split(',')
print(todos_list)
print(','.join(todos_list))

str1='jieer'
str2='is good!'
strtem= str1+" "+str2+"........."

print(strtem.count('is'))
print(strtem.startswith("Jieer1"))
print(strtem.endswith("..."))
print(strtem.strip('.'))
print(strtem[1:-5])

print(strtem.capitalize())

print(strtem.title())

print(strtem.upper())

print(strtem.swapcase())
print(strtem.center(5))

print(strtem.replace(' ',','))

print(len("Jieer" * 3))

print(str(98.5))

print('''jieer is good boy !!''')

print(int("34"))

print(float('1.0e4'))