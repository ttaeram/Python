N = int(input())

beehome = 1
cnt = 1
while N > beehome:
    beehome += 6 * cnt
    cnt += 1
print(cnt)
# 1
# 1 + 6
# 1 + 6 + 12
# 1 + 6 + 12 + 18