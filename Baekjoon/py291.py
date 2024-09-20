import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(1e6)] * 100001

def sol(n):
    arr[n] = 0
    res = []
    heapq.heappush(res, (0, n))

    while res:
        dis, pos = heapq.heappop(res)
        if arr[pos] < dis:
            continue
        for i in (pos-1, pos+1, pos*2):
            if i < 0 or i > 100000:
                continue
            cost = dis
            if i != pos*2:
                cost = dis + 1
            if cost < arr[i]:
                arr[i] = cost
                heapq.heappush(res, (cost, i))
        
sol(N)
print(arr[K])
