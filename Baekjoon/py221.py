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

while commands:
    X, C = commands.popleft()
    for x in range(X):