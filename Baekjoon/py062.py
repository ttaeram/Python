rep = int(input())

for r in range(1, rep + 1):
    print(' ' * (rep - r) + '*' * ((r-1) * 2 + 1))