import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    for j in map(int, input().split()):
        heapq.heappush(arr, -j)

for a in range(N):
    b = heapq.heappop(arr)
print(-b)