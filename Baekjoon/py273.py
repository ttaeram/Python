from collections import deque
import sys
input = sys.stdin.readline

def sol(start, end):
    path = [int(1e9)] * (N + 1)
    path[start] = 0
    semi = deque()
    semi.append((start, 0))
    while semi:
        a, b = semi.popleft()
        if b <= path[a]:
            for i in range(len(arr[a])):
                t, c = arr[a][i]
                if path[t] > path[a] + c:
                    path[t] = path[a] + c
                    semi.append((t, path[a]))
    return path[end]

N, E = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
v1, v2 = map(int, input().split())

case1 = sol(1, v1) + sol(v1, v2) + sol(v2, N)
case2 = sol(1, v2) + sol(v2, v1) + sol(v1, N)

if case1 >= int(1e9) and case2 >= int(1e9):
    print(-1)
else:
    print(min(case1, case2))