import sys
input = sys.stdin.readline

def sol(n):
    if len(n_arr) == M:
        print(*n_arr)
        return
    check = 0
    for i in range(n, N):
        if check != arr[i]:
            n_arr.append(arr[i])
            check = arr[i]
            sol(i)
            n_arr.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
n_arr = []
sol(0)