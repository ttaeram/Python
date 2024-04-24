from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 1]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def sol():
    M, N, H = map(int, input().split())
    arr = []
    ik = deque()
    anik = set()
    ikik = set()
    for h in range(H):
        arr_ = [list(map(int, input().split())) for _ in range(N)]
        arr.append(arr_)
        for r in range(N):
            for c in range(M):
                if arr[h][r][c] == 1:
                    ik.append((h, r, c, 0))
                elif arr[h][r][c] == 0:
                    anik.add((h, r, c))

    ans = 0
    while ik:
        h, r, c, t = ik.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and arr[h][nr][nc] == 0:
                arr[h][nr][nc] = 1
                ans = max(ans, t + 1)
                ik.append((h, nr, nc, t + 1))
                ikik.add((h, nr, nc))
        for j in range(2):
            nh = h + dh[j]
            if 0 <= nh < H and arr[nh][r][c] == 0:
                arr[nh][r][c] = 1
                ans = max(ans, t + 1)
                ik.append((nh, r, c, t + 1))
                ikik.add((nh, r, c))

    if anik != ikik:
        ans = -1

    print(ans)
sol()