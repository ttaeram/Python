import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
seats = [[0] * N for _ in range(N)]
check = [[] for _ in range(N**2 + 1)]
for i in range(N**2):
    stu, a, b, c, d = map(int, input().split())
    check[stu] = [a, b, c, d]
    if i == 0:
        seats[1][1] = stu
    else:
        stack = []
        for x in range(N):
            for y in range(N):
                if seats[x][y] == 0:
                    cnt_s = 0
                    cnt_0 = 0
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if seats[nx][ny] in check[stu]:
                                cnt_s += 1
                            if seats[nx][ny] == 0:
                                cnt_0 += 1
                    stack.append((cnt_s, cnt_0, x, y))
        stack.sort(key=lambda xy: (-xy[0], -xy[1], xy[2]))
        xxx, yyy, r, c = stack[0]
        seats[r][c] = stu
ans = 0
for r in range(N):
    for c in range(N):
        st = seats[r][c]
        cnt = 0
        for j in range(4):
            nr = r + dx[j]
            nc = c + dy[j]
            if 0 <= nr < N and 0 <= nc < N:
                if seats[nr][nc] in check[st]:
                    cnt += 1
        if cnt == 0:
            continue
        else:
            ans += 10 ** (cnt - 1)
print(ans)