N = int(input())
M = int(input())
arr = [[] for _ in range(N + 1)]

for m in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

stack = [1]
visited = [0] * (N + 1)
cnt = 0
while stack:
    num = stack.pop()
    if visited[num] == 0:
        visited[num] = 1
        cnt += 1

        for i in arr[num][::-1]:
            stack.append(i)
print(cnt - 1)