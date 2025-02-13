import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def sol():
    ans = 0
    while True:
        queue = deque()
        ch = [[0 for _ in range(M)] for _ in range(N)]
        ch[0][0] = 1
        queue.append([0, 0])

        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0 <= nc < M and not ch[nr][nc]:
                    if arr[nr][nc]:
                        arr[nr][nc] += 1
                    else:
                        ch[nr][nc] = 1
                        queue.append((nr, nc))

        flag = 0
        for x in range(N):
            for y in range(M):
                if arr[x][y] >= 3:
                    arr[x][y] = 0
                elif 0 < arr[x][y]:
                    flag = 1
                    arr[x][y] = 1
        ans += 1

        if not flag:
            return ans

ans = sol()
print(ans)