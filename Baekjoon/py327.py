import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def outside_air():
    queue = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    arr[0][0] = -1

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = -1
                    queue.append((nr, nc))
                visited[nr][nc] = True

def check(r, c):
    cnt = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == -1:
            cnt += 1
    return cnt >= 2

def expand_air(queue):
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = -1
                queue.append((nr, nc))

def sol():
    outside_air()
    ans = 0 

    while True:
        melting = []
        cheese_exist = False
        queue = deque()

        for r in range(N):
            for c in range(M):
                if arr[r][c] == 1:
                    cheese_exist = True
                    if check(r, c):
                        melting.append((r, c))

        if not cheese_exist:
            return ans
        
        for r, c in melting:
            arr[r][c] = -1
            queue.append((r, c))

        expand_air(queue)

        ans += 1

ans = sol()
print(ans)