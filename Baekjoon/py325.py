import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

def sol(r):
    cost = [-1] * (N + 1)
    route = deque([r])
    cost[r] = 0
    far = r

    while route:
        now = route.popleft()
        co = cost[now]

        for i in range(len(arr[now])):
            n, c = arr[now][i]
            if cost[n] == -1:
                cost[n] = c + co
                route.append(n)
                
                if cost[far] < cost[n]:
                    far = n

    return far, cost[far]

far, _ = sol(1)
_, ans = sol(far)

print(ans)