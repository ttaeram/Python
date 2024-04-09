from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

stack = deque([(0, 0)])
answer = []
def maze():
    while stack:
        x, y = stack.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                stack.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1
    return arr[N-1][M-1]
ans = maze()
print(ans)