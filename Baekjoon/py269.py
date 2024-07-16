import sys
input = sys.stdin.readline
from collections import deque

def move(x, y):
    semi.append((x, y))
    country = deque()
    country.append((x, y))
    while semi:
        r, c = semi.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in check:
                if L <= abs(arr[r][c] - arr[nr][nc]) <= R:
                    check.add((nr, nc))
                    semi.append((nr, nc))
                    country.append((nr, nc))
    
    if len(country) <= 1:
        return 0
    res = 0
    for c in country:
        res += arr[c[0]][c[1]]
    res //= len(country)
    for c in country:
        arr[c[0]][c[1]] = res
    return 1

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
semi = deque()
ans = 0
while True:
    cnt = 0
    check = set()
    for r in range(N):
        for c in range(N):
            if (r, c) not in check:
                check.add((r, c))
                cnt += move(r, c)
    if cnt == 0:
        break
    ans += 1
print(ans)