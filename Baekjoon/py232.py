from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

R, C = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(R)]

check = set()
ans_v = 0
ans_o = 0

for r in range(R):
    for c in range(C):
        if arr[r][c] == '.' or arr[r][c] == 'v' or arr[r][c] == 'o':
            if (r, c) not in check:
                cnt_v = 0
                cnt_o = 0
                stack = deque([(r, c)])
                while stack:
                    x, y = stack.popleft()
                    if (x, y) not in check:
                        check.add((x, y))
                        if arr[x][y] == 'v':
                            cnt_v += 1
                        elif arr[x][y] == 'o':
                            cnt_o += 1
                        for i in range(4):
                            nx = x + dx[i]
                            ny = y + dy[i]
                            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != '#':
                                stack.append((nx, ny))
                if cnt_o > cnt_v:
                    ans_o += cnt_o
                else:
                    ans_v += cnt_v

print(ans_o, ans_v)