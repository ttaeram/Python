import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N)]
for n in range(N):
    semi = list(map(int, input().split()))
    for m in range(N):
        if semi[m] == 1:
            arr[n].append(m)

c_arr = []
for x in range(N):
    stack = [x]
    check = [0] * N
    while stack:
        pos = stack.pop()
        for i in arr[pos]:
            if check[i] == 0:
                check[i] = 1
                stack.append(i)
    print(*check)