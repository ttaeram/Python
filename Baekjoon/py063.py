rep = int(input())

for r in range(1, rep + 1):
    print(' ' * (r - 1) + '*' * ((rep - r + 1) * 2 - 1))