from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
narr = [[0] * M for _ in range(N)]

for n in range(N):
    for m in range(M):
        if arr[n][m] == 2:
            start = (n, m, 0)
stack = deque([start])

while stack:
    x, y, d = stack.popleft()
    if not check[x][y]:
        check[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    check[nx][ny] = 1
                    continue
                if not check[nx][ny]:
                    nd = d + 1
                    narr[nx][ny] = nd
                    stack.append((nx, ny, nd))

for r in range(N):
    for c in range(M):
        if not check[r][c] and arr[r][c] != 0:
            narr[r][c] = -1

for a in range(N):
    for b in range(M):
        print(narr[a][b], end = ' ')
    print()