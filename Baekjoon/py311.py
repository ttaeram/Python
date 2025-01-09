from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

directions = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [(0, 1), (1, 2), (2, 3), (3, 0)],
    4: [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
    5: [(0, 1, 2, 3)]
}

def init():
    cctv = deque()
    ans = 0
    
    for r in range(N):
        for c in range(M):
            if arr[r][c] not in (0, 6):
                cctv.append((arr[r][c], r, c))
            
            if arr[r][c] == 0:
                ans += 1

    return cctv, ans

cctv, ans = init()

def move(r, c, direc, arr_copy):
    for d in direc:
        nr, nc = r, c

        while True:
            nr += dr[d]
            nc += dc[d]

            if 0 > nr or N <= nr or 0 > nc or M <= nc or arr_copy[nr][nc] == 6:
                break

            if arr_copy[nr][nc] != 0:
                continue

            arr_copy[nr][nc] = 7

def counting(arr_copy):
    global ans
    cnt = 0

    for i in arr_copy:
        cnt += i.count(0)
    
    ans = min(ans, cnt)

def sol(idx, arr_):
    arr_copy = [[c for c in arr_[r]] for r in range(N)]

    if idx == len(cctv):
        counting(arr_copy)
        return
    
    cc, r, c = cctv[idx]

    for direc in directions[cc]:
        move(r, c, direc, arr_copy)
        sol(idx + 1, arr_copy)
        arr_copy = [[j for j in arr_[i]] for i in range(N)]

sol(0, arr)
print(ans)