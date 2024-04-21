from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
odd = ('R', 'G')

N = int(input())
arr = [list(map(str, input().strip())) for _ in range(N)]
check = set()
cnt_1 = 0
cnt_2 = 0

def sol(r, c):
    stack = deque([(r, c)])
    check.add((r, c))
    while stack:
        x, y = stack.popleft()
        color = arr[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == color and (nx, ny) not in check:
                    check.add((nx, ny))
                    stack.append((nx, ny))

for r in range(N):
    for c in range(N):
        if (r, c) not in check:
            sol(r, c)
            cnt_1 += 1

check = set()
for r in range(N):
    for c in range(N):
        if arr[r][c] == 'R':
            arr[r][c] = 'G'

for r in range(N):
    for c in range(N):
        if (r, c) not in check:
            sol(r, c)
            cnt_2 += 1

print(cnt_1, cnt_2)
