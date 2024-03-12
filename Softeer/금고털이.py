import sys
input = sys.stdin.readline

W, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: -x[1])
res = 0
for i in range(N):
    if arr[i][0] <= W:
        res += arr[i][0] * arr[i][1]
        W -= arr[i][0]
    elif arr[i][0] > W:
        res += W * arr[i][1]
        break

print(res)