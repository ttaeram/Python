import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [(0, 0)]
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

dp = [[0] * (K + 1) for _ in range(N + 1)]
for n in range(1, N + 1):
    for k in range(1, K + 1):
        w = arr[n][0]
        v = arr[n][1]
        if w <= k:
            dp[n][k] = max(dp[n-1][k], dp[n-1][k-w] + v)
        else:
            dp[n][k] = dp[n-1][k]
print(dp[N][K])