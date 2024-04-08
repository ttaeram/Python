import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d_dic = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

N, M = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
while True:
    if arr[x][y] == 0:
        arr[x][y] = 1
        cnt += 1
    stack = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                stack.append((nx, ny))
    if not stack:
        x += d_dic[d][0]
        y += d_dic[d][1]
    else:
        
    if x < 0 or x >= N or y < 0 or y >= M:
        break