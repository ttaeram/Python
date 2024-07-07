import sys
input = sys.stdin.readline

N = int(input())
arr = [0]
for _ in range(N):
    T, P = map(int, input().split())
    arr.append((T, P))

dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1])
    res = i + arr[i][0] - 1
    if res <= N:
        dp[res] = max(dp[res], dp[i - 1] + arr[i][1])
print(max(dp))