N, M, V = map(int, input().split())
arr = [[] for _ in range(M)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
print(arr)
stack = [V]
visited = [0] * (N + 1)
while stack:
    num = stack.pop()
    if visited[num] == 0:
        visited[num] = 1
        print(num)

        for i in arr[num][::-1]:
            stack.append(i)