from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

stack = deque([(0, 0, 0)])
answer = []
while stack:
    x, y, d = stack.pop()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
            stack.append((nx, ny, d + 1))
            arr[nx][ny] = 0
            if nx == N and ny == M:
                answer.append(d)

print(answer)