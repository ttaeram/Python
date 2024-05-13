from collections import deque

def solution(m, n, puddles):
    dx = [0, 1]
    dy = [1. 0]
    arr = [[0] * m for _ in range(n)]
    for i in range(len(puddles)):
        a, b = puddles[i][0] - 1, puddles[i][1] - 1
        arr[a][b] = -1
    
    stack = deque([(0, 0, 0)])
    while stack:
        x, y, d = stack.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < n and ny < m:

    return answer

puddles = [[2, 2]]
print(solution(4, 3, puddles))