import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def sol(a, b):
    if b == 1:
        return a % C
    else:
        n = sol(a, b//2)
        if b % 2 == 0:
            return (n * n) % C
        else:
            return ((n * n) % C) * a % C

ans = sol(A, B)
print(ans)