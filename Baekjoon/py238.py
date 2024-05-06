import sys
input = sys.stdin.readline

def sol():
    if len(n_arr) == M:
        print(*n_arr)
        return
    flag = 0
    for i in range(N):
        if i not in check and flag != arr[i]:
            check.add(i)
            n_arr.append(arr[i])
            flag = arr[i]
            sol()
            check.remove(i)
            n_arr.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
check = set()
n_arr = []
sol()