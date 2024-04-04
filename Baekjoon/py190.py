import sys
input = sys.stdin.readline

N = int(input())
arr = [input().strip() for _ in range(N)]

dr = [1, 0, -1, 0, 1, 1, -1, -1]
dc = [0, 1, 0, -1, 1, -1, 1, -1]

new = [[0] * N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if arr[r][c].isdecimal():
            new[r][c] = '*'
        else:
            cnt = 0
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc].isdecimal():
                        cnt += int(arr[nr][nc])
            if cnt > 9:
                new[r][c] = 'M'
            else:
                new[r][c] = cnt
for a in new:
    print(*a, sep='')