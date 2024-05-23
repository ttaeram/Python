from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
arr = []
shark = tuple()
for r in range(N):
    a = list(map(int, input().split()))
    if not shark:
        for c in range(N):
            if a[c] == 9:
                shark = (r, c, 2, 0, 0)
                break
    arr.append(a)
check = set()
stack = deque([shark])
while stack:
    x, y, s, c, t = stack.pop()
    if (x, y) not in check:
        print((x, y, s, c, t))
        check.add((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] <= s:
                if arr[nx][ny] == 0:
                    stack.append((nx, ny, s, c, t + 1))
                else:
                    arr[nx][ny] = 0
                    if s == c + 1:
                        stack.append((nx, ny, s + 1, 0, t + 1))
                    else:
                        stack.append((nx, ny, s, c + 1, t + 1))
print(t-1)