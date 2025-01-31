import sys
import heapq
input = sys.stdin.readline

N, M, R = map(int, input().split())
items = list(map(int, input().split()))
arr = [[] for _ in range(N + 1)]

for _ in range(R):
    a, b, l = map(int, input().split())
    arr[a].append((b, l))
    arr[b].append((a, l))

def daik():
    ans = 0

    for i in range(1, N + 1):
        d = [int(1e9)] * (N + 1)
        q = []
        heapq.heappush(q, (0, i))
        d[i] = 0

        while q:
            dis, pos = heapq.heappop(q)

            if d[pos] < dis:
                continue

            for j in arr[pos]:
                cost = dis + j[1]

                if cost < d[j[0]]:
                    d[j[0]] = cost
                    heapq.heappush(q, (cost, j[0]))
        
        res = 0
        for idx, dd in enumerate(d):
            if dd <= M:
                res += items[idx - 1]
        
        ans = max(res, ans)

    return ans

ans = daik()
print(ans)