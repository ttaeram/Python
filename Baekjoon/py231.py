import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])
res = []
for a, b in arr:
    if not res:
        heapq.heappush(res, b)
    else:
        if res[0] > a:
            heapq.heappush(res, b)
        else:
            heapq.heappop(res)
            heapq.heappush(res, b)
print(len(res))
