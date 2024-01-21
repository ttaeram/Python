rep = int(input())

rep * 2 - 1
for star in range(1, rep + 1):
    print(' ' * (rep - star) + '*' * (star * 2 - 1))

for star_b in range(rep-1, 0, -1):
    print(' ' * (rep - star_b) + '*' * (star_b * 2 - 1))