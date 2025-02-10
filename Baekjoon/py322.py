import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
check = [int(1e9)] * (V + 1)
q = []
arr = [[] for _ in range(V + 1)]

def daik(idx):
    check[idx] = 0
    heapq.heappush(q, (0, idx))

    while q:
        cost, pos = heapq.heappop(q)

        if check[pos] < cost:
            continue

        for c, next_pos in arr[pos]:
            next_cost = c + cost

            if next_cost < check[next_pos]:
                check[next_pos] = next_cost
                heapq.heappush(q, (next_cost, next_pos))

for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((w, v))

daik(K)

for i in range(1, V + 1):
    if check[i] == int(1e9):
        print("INF")
    
    else:
        print(check[i])