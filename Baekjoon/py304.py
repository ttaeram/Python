from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def sol():
    Q = deque()
    semi = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if semi[i][j] == 2:
                Q.append((i, j))
    
    while Q:
        r, c = Q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if semi[nr][nc] == 0:
                semi[nr][nc] = 2
                Q.append((nr, nc))

    global ans
    cnt = 0

    for i in range(N):
        cnt += semi[i].count(0)
    
    ans = max(ans, cnt)

def wall(cnt):
    if cnt == 3:
        sol()
        return
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt + 1)
                arr[i][j] = 0

ans = 0
wall(0)

print(ans)