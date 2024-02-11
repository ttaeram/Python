def C_P(line):
    if line == 1:
        return 1
    if line == 2:
        return 3
    if line % 2 == 0:
        return C_P(line - 2) * 4 - 1
    elif line % 2 == 1:
        return C_P(line -2) * 4 + 1

N = int(input())
line = N

result = C_P(line) % 10007
print(result)