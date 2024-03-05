N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direction = [-1, 0, 1]

def path(col, row, d, low, ans):
    if col == N - 1:
        return min(low, ans)
    for i in direction:
        if i != d:
            if 0 <= col < N and 0 <= row + i < M:
                low = path(col + 1, row + i, i, low, ans + arr[col + 1][row + i])
    return low

low = 1000
for i in range(M):
    low = min(path(0, i, 2, low, arr[0][i]), low)

print(low)