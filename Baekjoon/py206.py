import sys
input = sys.stdin.readline

direction = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = []
for _ in range(M):
    d, s = map(int, input().split())
    command.append((d, s))

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]

cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
for m in range(M):
    check = []
    com = command[m]
    d, s = com
    for c in cloud:
        x, y = c
        cx = (x + direction[d][0] * s) % N
        cy = (y + direction[d][1] * s) % N
        check.append((cx, cy))
        arr[cx][cy] += 1
    for cl in check:
        ccx, ccy = cl
        cnt = 0
        for i in range(4):
            nx = ccx + dx[i]
            ny = ccy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > 0:
                    cnt += 1
        arr[ccx][ccy] += cnt
    cloud = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] >= 2 and (r, c) not in check:
                arr[r][c] -= 2
                cloud.append((r, c))
ans = 0
for n in range(N):
    ans += sum(arr[n])
print(ans)