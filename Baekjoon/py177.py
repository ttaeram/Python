import sys
from collections import deque
input = sys.stdin.readline

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bug = deque()
                bug.append((i, j))
                arr[i][j] = 0
                while bug:
                    a, b = bug.popleft()

                    for k in range(4):
                        ni = a + di[k]
                        nj = b + dj[k]
                        if 0 <= ni < N and 0 <= nj < M:
                            if arr[ni][nj] == 1:
                                bug.append((ni, nj))
                                arr[ni][nj] = 0
                cnt += 1

    print(cnt)