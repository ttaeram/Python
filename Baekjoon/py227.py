import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

arr = []
for n in range(N):
    if n == 0:
        arr.append(cost[n])
    else:
        arr.append(cost[n])
        arr[n][0] += min(arr[n-1][1], arr[n-1][2])
        arr[n][1] += min(arr[n-1][0], arr[n-1][2])
        arr[n][2] += min(arr[n-1][0], arr[n-1][1])
print(min(arr[N-1]))