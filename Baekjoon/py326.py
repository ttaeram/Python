import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

start, end = map(int, input().split())

def sol():
    INF = int(1e9)
    cost = [[INF] for _ in range(N + 1)]
    cost[start] = [0, start]
    route = [(0, start)]

    while route:
        co, now = heapq.heappop(route)

        if now == end:
            return cost[now]

        for n, c in arr[now]:
            new_c = c + co
        
            if new_c < cost[n][0]:
                cost[n] = [new_c] + cost[now][1:] + [n]
                heapq.heappush(route, (new_c, n))

    return cost[end]

route = sol()

a1 = route[0]
a2 = len(route) - 1
a3 = route[1:]

print(a1)
print(a2)
print(*a3)