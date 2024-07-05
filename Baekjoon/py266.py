import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    T, P = map(int, input().split())
    arr.append((T, P))
ans = 0
for n in range(N):
    dp = [0] * N
    while True:
        if (n + arr[n][0]) < N:
            dp[n + arr[n][0]] +=( arr[n][1] + dp[n])
            print(arr[n][0])