from collections import deque

# 그래프 정의
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


# DFS - 재귀 방식
def dfs_recursive(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs_recursive(graph, i, visited)


# DFS - 스택을 이용한 반복 방식
def dfs_stack(graph, start):
    visited = [0] * len(graph)
    stack = [start]

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')

            for i in reversed(graph[v]):
                if not visited[i]:
                    stack.append(i)


# BFS - 큐를 이용한 반복 방식
def bfs_queue(graph, start):
    visited = [0] * len(graph)
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


def init():
    print("DFS (재귀): ", end='')
    dfs_recursive(graph, 1, [0] * len(graph))
    print()


    print("DFS (스택): ", end='')
    dfs_stack(graph, 1)
    print()


    print("BFS (덱큐): ", end='')
    bfs_queue(graph, 1)
    print()


init()