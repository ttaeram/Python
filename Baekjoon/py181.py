import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]

for m in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

stack = []
arr_arr_arr = []
visited = [0] * (N + 1)

for i in range(1, N + 1):
    if visited[i] == 1:
        continue
    check = [0] * (N + 1)
    res = []
    stack.append(i)
        
    while stack:
        st = stack.pop()
        if check[st] == 0:
            check[st] = 1
            res.append(st)
            for j in arr[st]:
                stack.append(j)

    arr_arr_arr.append(res)
    for l in res:
        visited[l] = 1

print(len(arr_arr_arr))