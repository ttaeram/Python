import sys
input = sys.stdin.readline

def sol(n):
    if len(n_arr) == M:
        print(*n_arr)
        return
    for i in arr:
        if i not in n_arr:
            n_arr.append(i)
            sol(i + 1)
            n_arr.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
n_arr = []
sol(1)