x_max = 0
y_max = 0
paper = {}

N = int(input())
for n in range(1, N + 1):
    x_1, y_1, l, h = map(int, input().split())
    x_2 = x_1 + l
    y_2 = y_1 + h
    if x_max < x_2:
        x_max = x_2
    if y_max < y_2:
        y_max = y_2
    paper[n] = [x_1, y_1, x_2, y_2]

board = [[0] * x_max for _ in range(y_max)]

for i in range(1, N + 1):
    for j in range(paper[i][1], paper[i][3]):
        for k in range(paper[i][0], paper[i][2]):
            board[j][k] = i

cnt = [0] * (N)

for l in range(y_max):
    for m in range(x_max):
        for n in range(1, N + 1):
            if board[l][m] == n:
                cnt[n - 1] += 1

print(*cnt, sep = '\n')