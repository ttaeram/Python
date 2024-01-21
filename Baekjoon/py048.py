S = input()

S_list = []
for s in S:
    S_list.append(ord(s))

alphabet = []
for i in range(ord('a'), ord('z') + 1):
    alphabet.append(i)

alphabet_1 = []
for a in alphabet:
    if a in S_list:
        alphabet_1.append(S_list.index(a))
    else:
        alphabet_1.append(-1)
for result in alphabet_1:
    print(result, end = ' ')