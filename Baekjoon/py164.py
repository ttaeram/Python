import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for n in range(N):
    command = int(input())
    if command == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, command)