import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]
d = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)}
fire = []
for m in range(M):
    ri, ci, mi, si, di = map(int, input().split())
    fire.append((ri - 1, ci - 1, mi, si, di))

for k in range(K):
    while fire:
        r, c, m, s, dd = fire.pop(0)
        dr = s * d[dd][0]
        dc = s * d[dd][1]
        nr = (r + dr + N) % N
        nc = (c + dc + N) % N
        arr[nr][nc].append((m, s, dd))

    for r in range(N):
        for c in range(N):
            if len(arr[r][c]) > 1:
                l = len(arr[r][c])
                m, s, cnt_odd, cnt_eve = 0, 0, 0, 0
                while arr[r][c]:
                    mm, ss, dd = arr[r][c].pop(0)
                    m += mm
                    s += ss
                    if dd % 2 == 0:
                        cnt_eve += 1
                    else:
                        cnt_odd += 1
                m = m // 5
                s = s // l
                if m > 0:
                    if cnt_eve == l or cnt_odd == l:
                        dl = [0, 2, 4, 6]
                    else:
                        dl = [1, 3, 5, 7]
                    for i in dl:
                        fire.append((r, c, m, s, i))

            if len(arr[r][c]) == 1:
                m, s, dd = arr[r][c].pop()
                fire.append((r, c, m, s, dd))

ans = 0
for a in fire:
    ans += a[2]
print(ans)