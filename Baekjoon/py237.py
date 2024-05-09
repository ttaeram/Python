import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    for j in map(int, input().split()):
        if len(arr) == N and min(arr) < j:
            heapq.heappop(arr)
            heapq.heappush(arr, j)
        elif len(arr) < N:
            heapq.heappush(arr, j)

ans = arr[0]
print(ans)