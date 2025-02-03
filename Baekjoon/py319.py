import sys
input = sys.stdin.readline

M = int(input())
info = []
MOD = 1000000007

def sol(N, X):
    if X == 1:
        return N
    
    num = sol(N, X//2)

    if X % 2 == 0:
        return num * num % MOD
    
    else:
        return num * num * N % MOD

ans = 0
for _ in range(M):
    n, s = map(int, input().split())
    res = sol(n, MOD - 2)
    ans = (ans + res * s % MOD) % MOD

print(ans)