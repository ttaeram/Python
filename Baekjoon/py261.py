from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
for k in range(K):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1

L = int(input())
commands = {}
for l in range(L):
    X, C = input().split()
    commands[int(X)] = C

snake = deque()
snake.append((0, 0))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y, t, d = 0, 0, 0, 0

arr[0][0] = 2
while True:
    t += 1
    x += dx[d]
    y += dy[d]
    if x < 0 or x >= N or y <0 or y >= N:
        break

    if arr[x][y] == 1:
        arr[x][y] = 2
        snake.append((x, y))
        if t in commands.keys():
            if commands[t] == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
    elif arr[x][y] == 0:
        arr[x][y] = 2
        snake.append((x, y))
        px, py = snake.popleft()
        arr[px][py] = 0
        if t in commands.keys():
            if commands[t] == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
    else:
        break

print(t)