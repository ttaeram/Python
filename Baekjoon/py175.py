from collections import deque
N, M, V = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
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
stack_2 = deque(stack_2)
BFS = []
visited_2 = [0] * (N + 1)
while stack_2:
    num_1 = stack_2.popleft()
    if visited_2[num_1] == 0:
        visited_2[num_1] = 1
        BFS.append(num_1)

        for j in arr[num_1]:
            stack_2.append(j)
print(*BFS)