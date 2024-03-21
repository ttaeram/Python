from random import *
pictures = set()
while True:
    name = input()
    if name == '0':
        break
    if name in pictures:
        print(f'{name}은 이미 있습니다')
    pictures.add(name)

print(len(pictures))