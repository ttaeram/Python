croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for w in croa:
    if w in word:
        word = word.replace(w, '씹')

print(len(word))