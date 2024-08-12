from math import floor
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
start = N//2
dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def wind(x, y, dx, dy):
    if not (0 <= x + dx < N and 0 <= y + dy < N):
        return 0
    
    total = arr[x + dx][y + dy]
    cand = []
    cand.append((x + dx * 3, y + dy * 3, 0.05))
    if dx == 0:
        cand.append((x + 1, y + dy * 2, 0.1))
        cand.append((x - 1, y + dy * 2, 0.1))
        cand.append((x + 1, y + dy, 0.07))
        cand.append((x - 1, y + dy, 0.07))
        cand.append((x + 2, y + dy, 0.02))
        cand.append((x - 2, y + dy, 0.02))
        cand.append((x + 1, y, 0.01))
        cand.append((x - 1, y, 0.01))
    else:
        cand.append((x + dx * 2, y + 1, 0.1))
        cand.append((x + dx * 2, y - 1, 0.1))
        cand.append((x + dx, y + 1, 0.07))
        cand.append((x + dx, y - 1, 0.07))
        cand.append((x + dx, y + 2, 0.02))
        cand.append((x + dx, y - 2, 0.02))
        cand.append((x, y + 1, 0.01))
        cand.append((x, y - 1, 0.01))
    vals = 0
    res = 0
    for c in cand:
        val = floor(c[2] * total)
        a, b = c[0], c[1]
        if 0 <= a < N and 0 <= b < N:
            arr[a][b] += val
        else:
            res += val
        vals += val

    a, b = x + dx * 2, y + dy * 2
    if 0 <= a < N and 0 <= b < N:
        arr[a][b] += total - vals
    else:
        res += total - vals
    return res

def tornado(x, y, i):
    d, d1, d2 = 1, 0, 0
    ans = 0
    while x >= 0 and y >= 0:
        dx, dy = dir[i][0], dir[i][1]
        ans += wind(x, y, dx, dy)
        x += dx
        y += dy
        d1 += 1
        if d == d1:
            i = (i + 1) % 4
            if d2 == 0:
                d1, d2 = 0, d2 + 1
            else:
                d, d1, d2 = d + 1, 0, 0
    return ans

ans = tornado(start, start, 0)
print(ans)
