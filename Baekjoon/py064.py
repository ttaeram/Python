rep = int(input())

for r in range(rep):
    print('*' * (r + 1) + ' ' * ((rep - r - 1) * 2) + '*' * (r + 1))

for e in range(1, rep):
    print('*' * (rep - e) + ' ' * (2 * e) + '*' * (rep - e))