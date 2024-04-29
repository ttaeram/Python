import sys
input = sys.stdin.readline

def sol(n):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(n, N + 1):
        if i not in arr:
            arr.append(i)
            sol(i + 1)
            arr.pop()

N, M = map(int, input().split())
arr = []
sol(1)