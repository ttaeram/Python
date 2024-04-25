from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * N for _ in range(N)]
arr[0][0] = 2
K = int(input())
for k in range(K):
    a, b = map(int, input().split())
    arr[a][b] = 1
L = int(input())
commands = deque()
for l in range(L):
    a, b = map(str, input().split())
    commands.append((int(a), b))
stack = [(0, 0, 0, 1, 1)]
for co in commands:
    t, command = co
    for tt in range(t):
        while stack:
            r, c, dx, dy, l = stack.popleft()
            nr = r + dx
            nc = c + dy
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0:
                    