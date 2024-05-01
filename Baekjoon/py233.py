import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

check = set()
for r in range(N):
    for c in range(M):
        if (r, c) not in check:
            x, y = r, c
            d = (0, 1)
            stack_p = [(r, c)]
            stack_v = [arr[r][c]]
            while True:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < N and 0 <= ny < M:
                    if (nx, ny) not in check:
                        x, y = nx, ny
                    elif (nx, ny) in check and d[0] == 0:
                        d = (d[1], d[0])
                        x, y = x + d[0], y + d[1]
                    elif (nx, ny) in check and d[1] == 0:
                        d = (d[1], -d[0])
                        x, y = x + d[0], y + d[1]
                elif ny == M or ny == -1:
                    d = (d[1], d[0])
                    x, y = x + d[0], y + d[1]
                elif nx == N or nx == -1:
                    d = (d[1], -d[0])
                    x, y = x + d[0], y + d[1]
                if (x, y) == (r, c):
                    break
                check.add((x, y))
                stack_p.append((x, y))
                stack_v.append(arr[x][y])
            l = len(stack_v)
            a = R % l
            for b in range(a, l):
                arr[stack_p[(b - a) % l][0]][stack_p[(b - a) % l][1]] = stack_v[b]
            for b in range(a):
                arr[stack_p[(b - a) % l][0]][stack_p[(b - a) % l][1]] = stack_v[b]
for n in range(N):
    print(*arr[n])