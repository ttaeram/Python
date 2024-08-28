import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())

command = []
for _ in range(K):
    c, d = map(int, input().split())
    command.append((c-1, d))

arr = [[0] * C for _ in range(R+1)]

direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
ans = {}
drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
g_n = 1

while command:
    c, d = command.pop(0)
    r = 0
    cg = [d, [r-1, c], [r, c-1], [r, c], [r, c+1], [r+1, c]]
    cg = (r, c, d)
    cnt = 0
    while True:
        r, c, d = cg
        check = [0, 0, 0]
        if r+2 <= R and arr[r+1][c-1] == 0 and arr[r+2][c] == 0 and arr[r+1][c+1] == 0:
            cg = (r+1, c, d)
            check = [1, 0, 0]

        if check == [0, 0, 0]:
            if r == 0:
                if c-2 >= 0 and arr[r][c-2] == 0 and arr[r+1][c-1] == 0 and r+2 <= R and arr[r+1][c-2] == 0 and arr[r+2][c-1] == 0 and arr[r+1][c] == 0:
                    if d == 0:
                        d = 3
                    else:
                        d -= 1
                    cg = (r+1, c-1, d)
                    check = [0, 1, 0]
            else:
                if c-2 >= 0 and arr[r-1][c-1] == 0 and arr[r][c-2] == 0 and arr[r+1][c-1] == 0 and r+2 <= R and arr[r+1][c-2] == 0 and arr[r+2][c-1] == 0 and arr[r+1][c] == 0:
                    if d == 0:
                        d = 3
                    else:
                        d -= 1
                    cg = (r+1, c-1, d)
                    check = [0, 1, 0]

        if check == [0, 0, 0]:
            if r == 0:
                if c+2 < C and arr[r][c+2] == 0 and arr[r+1][c+1] == 0 and r+2 <= R and arr[r+1][c] == 0 and arr[r+2][c+1] == 0 and arr[r+1][c+2] == 0:
                    if d == 3:
                        d = 0
                    else:
                        d += 1
                    cg = (r+1, c+1, d)
                    check = [0, 0, 1]
            else:
                if c+2 < C and arr[r-1][c+1] == 0 and arr[r][c+2] == 0 and arr[r+1][c+1] == 0 and r+2 <= R and arr[r+1][c] == 0 and arr[r+2][c+1] == 0 and arr[r+1][c+2] == 0:
                    if d == 3:
                        d = 0
                    else:
                        d += 1
                    cg = (r+1, c+1, d)
                    check = [0, 0, 1]

        if check == [0, 0, 0]:
            if cnt == 0:
                break
            else:
                arr[r-1][c] = g_n
                arr[r][c-1] = g_n
                arr[r][c] = g_n
                arr[r][c+1] = g_n
                arr[r+1][c] = g_n

                if arr[0].count(0) != C:
                    cnt = 0
                    break

                exit_r = r+direction[d][0]
                exit_c = c+direction[d][1]

                cand = []
                for i in range(4):
                    nr = exit_r + drc[i][0]
                    nc = exit_c + drc[i][1]
                    if 0 <= nr <= R and 0 <= nc < C:
                        if arr[nr][nc] != 0 and arr[nr][nc] != g_n:
                            cand.append(ans[arr[nr][nc]])
                if cand:
                    ans[g_n] = max(cand)
                else:
                    ans[g_n] = r+1
                break
        cnt += 1

    if cnt == 0:
        arr = [[0] * C for _ in range(R+1)]
    g_n += 1
answer = sum(ans.values())
print(answer)