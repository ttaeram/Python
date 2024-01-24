N, B = map(str, input().split())

B = int(B)
alphabet = {}
for i in range(65, 91):
    alphabet[chr(i)] = i - 55

num = 0
for n in range(len(N)):
    if N[n].isdecimal() == True:
        num += int(N[n]) * (B ** (len(N) - n - 1))
    else:
        num += alphabet[N[n]] * (B ** (len(N) - n - 1))


print(num)