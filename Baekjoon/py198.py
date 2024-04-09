from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
arr = []
stack = deque([])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt_0 = 0
for n in range(N):
    a_p = list(map(int, input().split()))
    for m in range(M):
        if a_p[m] == 1:
            stack.append((n, m, 0))
        elif a_p[m] == 0:
            cnt_0 += 1
    arr.append(a_p)

while stack:
    x, y, t = stack.popleft()
    # if arr[x][y] == 0:
    #     arr[x][y] = 1
    #     cnt_0 -= 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
            arr[nx][ny] = 1
            cnt_0 -= 1
            stack.append((nx, ny, t + 1))
    time = t

if cnt_0 > 0:
    time = -1

print(time)