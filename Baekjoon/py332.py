import sys
input = sys.stdin.readline

N = int(input())

dp = {}

def sol(n):
    if dp.get(n):
        return dp[n]
    
    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    
    if n % 2 == 0:
        dp[n // 2 + 1] = sol(n // 2 + 1) % 1000000007
        dp[n // 2 - 1] = sol(n // 2 - 1) % 1000000007

        return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2
    
    else:
        dp[n // 2 + 1] = sol(n // 2 + 1) % 1000000007
        dp[n // 2] = sol(n // 2) % 1000000007

        return dp[n // 2 + 1] ** 2 + dp[n // 2] ** 2

ans = sol(N) % 1000000007
print(ans)