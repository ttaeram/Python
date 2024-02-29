from collections import Counter
import sys
input = sys.stdin.readline

cnt = 0
LS = []
N, M = map(int, input().split())
L = Counter(input().strip() for _ in range(N + M))
for l in L:
    if L[l] > 1:
        LS.append(l)
        cnt += 1
LS.sort()
print(cnt)
print(*LS, sep = '\n')
