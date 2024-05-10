import sys
input = sys.stdin.readline

def sol(n):
    if len(arr) == M:
        print(*arr)
    else:
        for i in range(1, N + 1):
            if i not in arr:
                arr.append(i)
                sol(i + 1)
                arr.pop()

N, M = map(int, input().split())
arr = []
sol(1)