import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for x in range(N):
    for y in range(M):
        a, b, c = y + 1, y + 2, y + 3
        if 0 <= c < M:
            ans = max(ans, arr[x][y] + arr[x][a] + arr[x][b] + arr[x][c])
        a, b, c = x + 1, x + 2, x + 3
        if 0 <= c < N:
            ans = max(ans, arr[x][y] + arr[a][y] + arr[b][y] + arr[c][y])
        a, b = x + 1, y + 1
        if 0 <= a < N and 0 <= b < M:
            ans = max(ans, arr[x][y] + arr[x][b] + arr[a][y] + arr[a][b])
        a, b, c = x + 1, y + 1, y + 2
        if 0 <= a < N and 0 <= c < M:
            ans = max(ans, arr[x][y] + arr[x][b] + arr[x][c] + arr[a][c])
            ans = max(ans, arr[x][y] + arr[x][b] + arr[x][c] + arr[a][y])
            ans = max(ans, arr[x][c] + arr[a][y] + arr[a][b] + arr[a][c])
            ans = max(ans, arr[x][y] + arr[a][y] + arr[a][b] + arr[a][c])
        a, b, c = x + 1, x + 2, y + 1
        if 0 <= b < N and 0 <= c < M:
            ans = max(ans, arr[x][y] + arr[x][c] + arr[a][y] + arr[b][y])
            ans = max(ans, arr[x][y] + arr[b][c] + arr[a][y] + arr[b][y])
        c = y - 1
        if 0 <= b < N and 0 <= c < M:
            ans = max(ans, arr[x][y] + arr[x][c] + arr[a][y] + arr[b][y])
            ans = max(ans, arr[x][y] + arr[b][c] + arr[a][y] + arr[b][y])
        a, b, c = y + 1, x + 1, x + 2
        if 0 <= a < M and 0 <= c < N:
            ans = max(ans, arr[x][y] + arr[b][y] + arr[b][a] + arr[c][a])
            ans = max(ans, arr[x][a] + arr[b][y] + arr[b][a] + arr[c][y])
        a, b, c = x + 1, y + 1, y + 2
        if 0 <= a < N and 0 <= c < M:
            ans = max(ans, arr[x][b] + arr[x][c] + arr[a][y] + arr[a][b])
            ans = max(ans, arr[x][y] + arr[x][b] + arr[a][b] + arr[a][c])
        a, b, c = x + 1, y + 1, y + 2
        if 0 <= a < N and 0 <= c < M:
            ans = max(ans, arr[x][b] + arr[a][y] + arr[a][b] + arr[a][c])
            ans = max(ans, arr[x][y] + arr[x][b] + arr[x][c] + arr[a][b])
        a, b, c = x + 1, x + 2, y + 1
        if 0 <= b < N and 0 <= c < M:
            ans = max(ans, arr[x][y] + arr[a][y] + arr[b][y] + arr[a][c])
            ans = max(ans, arr[x][c] + arr[a][y] + arr[a][c] + arr[b][c])
print(ans)