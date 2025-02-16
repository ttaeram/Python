import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for _ in range(N):
    semi = input().strip()
    arrr = []
    for m in range(M):
        arrr.append(int(semi[m]))
    
    arr.append(arrr)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

check = [[[0] * 2 for _ in range(M)] for _ in range(N)]
check[0][0][0] = 1

def sol(r, c, t):
    q = deque()
    q.append((r, c, t))

    while q:
        r, c, t = q.popleft()

        if r == N - 1 and c == M - 1:
            return check[r][c][t]
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and t == 0:
                    check[nr][nc][1] = check[r][c][0] + 1
                    q.append((nr, nc, 1))
                
                elif arr[nr][nc] == 0 and check[nr][nc][t] == 0:
                    check[nr][nc][t] = check[r][c][t] + 1
                    q.append((nr, nc, t))
    
    return -1

ans = sol(0, 0, 0)
print(ans)