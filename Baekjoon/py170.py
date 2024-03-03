import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))

def bingo_check():
    bingo = 0

    for x in arr:
        if x.count(0) == 5:
            bingo += 1
    
    for i in range(5):
        y = 0
        for j in range(5):
            if arr[j][i] == 0:
                y += 1
        if y == 5:
            bingo += 1
    
    xy = 0
    for k in range(5):
        if arr[k][k] == 0:
            xy += 1
    if xy == 5:
        bingo += 1
    
    yx = 0
    for l in range(5):
        if arr[l][4 - l] == 0:
            yx += 1
    if yx == 5:
        bingo += 1
    
    return bingo

cnt = 0
for m in range(25):
    for n in range(5):
        for o in range(5):
            if mc[m] == arr[n][o]:
                arr[n][o] = 0
                cnt += 1
    if cnt >= 12:
        ans = bingo_check()

        if ans >= 3:
            print(m + 1)
            break