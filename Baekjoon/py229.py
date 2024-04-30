import sys
input = sys.stdin.readline

N, M = map(int, input().split())
def sol(n):
    if len(arr) == M:
        print(*arr)
        return
    else:
        for i in range(1, N + 1):
            if arr and arr[-1] > i:
                continue
            else:
                arr.append(i)
                sol(i + 1)
                arr.pop()

arr = []
sol(1)