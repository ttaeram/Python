import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    for j in map(int, input().split()):
        heapq.heappush(arr, j)
        if len(arr) > N:
            heapq.heappop(arr)

ans = arr[0]
print(ans)