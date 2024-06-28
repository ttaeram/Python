import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
dice_noon = {1: [0, 4, 3, 2, 5, 6], 2: [0, 4, 3, 6, 1, 5], 3: [0, 6, 1, 5, 2, 4], 4: [0, 1, 6, 5, 2, 3], 5: [0, 4, 3, 1, 6, 2], 6: [0, 4, 3, 5, 2, 1]}
direction = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
arr = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dice = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0, 'front': 0, 'back': 0}

def roll_east(dice):
    return {
        'top': dice['left'],
        'bottom': dice['right'],
        'left': dice['bottom'],
        'right': dice['top'],
        'front': dice['front'],
        'back': dice['back']
    }

def roll_west(dice):
    return {
        'top': dice['right'],
        'bottom': dice['left'],
        'left': dice['top'],
        'right': dice['bottom'],
        'front': dice['front'],
        'back': dice['back']
    }

def roll_north(dice):
    return {
        'top': dice['front'],
        'bottom': dice['back'],
        'left': dice['left'],
        'right': dice['right'],
        'front': dice['bottom'],
        'back': dice['top']
    }

def roll_south(dice):
    return {
        'top': dice['back'],
        'bottom': dice['front'],
        'left': dice['left'],
        'right': dice['right'],
        'front': dice['top'],
        'back': dice['bottom']
    }
for c in command:
    dx, dy = direction[c]
    nx = x + dx
    ny = y + dy
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny

        if c == 1:
            dice = roll_east(dice)
        elif c == 2:
            dice = roll_west(dice)
        elif c == 3:
            dice = roll_north(dice)
        elif c == 4:
            dice = roll_south(dice)

        if arr[x][y] == 0:
            arr[x][y] = dice['bottom']
        else:
            dice['bottom'] = arr[x][y]
            arr[x][y] = 0
            
        print(dice['top'])
