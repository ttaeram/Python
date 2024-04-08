import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d_dic = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
cid_d = {(-1, 0): 0, (0, 1): 1, (1, 0): 2, (0, -1): 3}

N, M = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
while True:
    if arr[x][y] == 0:
        arr[x][y] = 2
        cnt += 1
    stack = [(-1, -1, -1)] * 4
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                stack[cid_d[(dx[i], dy[i])]] = (nx, ny, cid_d[(dx[i], dy[i])])

    if stack == [(-1, -1, -1)] * 4:
        x -= d_dic[d][0]
        y -= d_dic[d][1]
    else:
        # if stack[d] == (-1, -1, -1):
        nd = (d + 3) % 4
        if stack[nd] == (-1, -1, -1):
            while True:
                nd = (nd + 3) % 4
                if stack[nd] != (-1, -1, -1):
                    break
            x, y, d = stack[nd]
        else:
            x, y, d = stack[nd]
        # else:
        #     x, y, d = stack[d]

    if arr[x][y] == 1:
        break

print(cnt)