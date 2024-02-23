board = [[0] * 100 for _ in range(100)]
cnt = 0

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            board[k][j] = 1

for m in range(100):
    for n in range(100):
        if board[n][m] == 1:
            cnt += 1

print(cnt)