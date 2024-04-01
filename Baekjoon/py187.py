from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)
res = [int(1e9)] * (N + 1)
stack = deque()
stack.append((X, 0))
while stack:
    pos, cnt = stack.popleft()
    if arr[pos]:
        for i in range(len(arr[pos])):
            if cnt + 1 > K:
                continue
            stack.append((arr[pos][i], cnt + 1))
            res[arr[pos][i]] = min(res[arr[pos][i]], cnt + 1)

flag = True
for n in range(N + 1):
    if res[n] == K:
        print(n, end = '\n')
        flag = False

if flag:
    print(-1)