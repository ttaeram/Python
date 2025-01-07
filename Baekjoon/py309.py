import sys
input = sys.stdin.readline

N = int(input())
O1, O2 = map(int, input().split())
U = int(input())
arr = [int(input()) for _ in range(U)]

dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

def sol(i, d1, d2):
    if i == U:
        return 0
    
    res = arr[i]

    dp[res][d1][d2] = min(
        abs(res - d1) + sol(i + 1, res, d2), abs(res - d2) + sol(i + 1, d1, res)
    )

    return dp[res][d1][d2]

ans = sol(0, O1, O2)
print(ans)