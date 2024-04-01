from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)
check = [0] * (N + 1)
res = [int(1e9)] * (N + 1)
stack = deque()
stack.append((X, 0))
check[X] = 1
while stack:
    pos, cnt = stack.popleft()
    for i in arr[pos]:
        if cnt + 1 > K:
            continue
        if check[i] == 0:
            check[i] = 1
            stack.append((i, cnt + 1))
            res[i] = min(res[i], cnt + 1)

flag = True
for n in range(N + 1):
    if res[n] == K:
        print(n, end = '\n')
        flag = False

if flag:
    print(-1)