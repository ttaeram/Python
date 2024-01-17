S = str(input())
asc = []

for _ in range(len(S)):
    asc.append(S[_])

for _ in asc:
    asc[_] = ord(asc[_])
print(asc)
'''
alphabet = list(range(97, 123))
for _ in alphabet:
    if asc[_] == alphabet[_]:
        alphabet[_] = (asc[_]).index
    else:
        alphabet[_] = -1
print(alphabet)     #a = 97 z = 122
'''