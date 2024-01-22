rep = int(input())

for r in range(1, rep + 1):
    print(' ' * (r - 1) + '*' * ((rep - r) * 2 + 1))

for e in range(1, rep):
    print(' ' * (rep - 1 - e) + '*' * (2 * e + 1))