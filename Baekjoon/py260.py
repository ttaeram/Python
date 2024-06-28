import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
dice_noon = {1: [0, 4, 3, 2, 5, 6], 2: [0, 4, 3, 6, 1, 5], 3: [0, 6, 1, 5, 2, 4], 4: [0, 1, 6, 5, 2, 3], 5: [0, 4, 3, 1, 6, 2], 6: [0, 4, 3, 5, 2, 1]}
direction = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
arr = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dice = 1
for c in command:
    dx, dy = direction[c]
    nx = x + dx
    ny = y + dy
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
    else:
        continue

    dice = dice_noon[dice][c]
    if arr[x][y] == 0:
        arr[x][y] = dice_noon[dice_noon[dice][5]][0]
    else:
        dice_noon[dice_noon[dice][5]][0] = arr[x][y]
        arr[x][y] = 0
    print(dice_noon[dice][0])
