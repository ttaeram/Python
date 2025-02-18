import sys
from collections import deque
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for m in range(M):
    a, b, t = map(int, input().split())
    arr[a].append((b, t))

def sol(start):
    q = []
    heapq.heappush(q, (0, start))

    route = [int(1e9)] * (N + 1)
    route[start] = 0

    while q:
        c, pos = heapq.heappop(q)

        if route[pos] >= c:
            for b, t in arr[pos]:
                if c + t < route[b]:
                    route[b] = c + t
                    heapq.heappush(q, (c + t, b))
    
    return route

res = sol(X)
res[0] = 0

for i in range(1, N + 1):
    if i != X:
        semi = sol(i)
        res[i] += semi[X]

ans = max(res)
print(ans)