import sys
input = sys.stdin.readline

direction = {
    (0, 1): [(-1, 1), (0, 1), (1, 1)],
    (1, 1): [(0, 1), (1, 1), (1, 0)],
    (1, 0): [(1, 1), (1, 0)]
    }

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

for i in range(N):
    if arr[0][i]:
        break
    else:
        dp[0][i][0] = 1

for i in range(1, N):
    for j in range(2, N):
        if arr[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]

            if arr[i-1][j] == 0 and arr[i][j-1] == 0:
                dp[i][j][1] = sum(dp[i-1][j-1])
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]

print(sum(dp[N-1][N-1]))
