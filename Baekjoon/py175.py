from collections import deque
N, M, V = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
print(arr)
for l in arr:
    l.sort()

stack = [V]
DFS = []
visited = [0] * (N + 1)
while stack:
    num = stack.pop()
    if visited[num] == 0:
        visited[num] = 1
        DFS.append(num)

        for i in arr[num][::-1]:
            stack.append(i)
print(*DFS)

stack_2 = [V]
BFS = deque()
visited_2 = [0] * (N + 1)
