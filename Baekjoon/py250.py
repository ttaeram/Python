import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
n_arr = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        n_arr[i][j] = n_arr[i][j-1] + n_arr[i-1][j] - n_arr[i-1][j-1] + arr[i-1][j-1]

for m in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = n_arr[x2][y2] - n_arr[x2][y1-1] - n_arr[x1-1][y2] + n_arr[x1-1][y1-1]
    print(ans)