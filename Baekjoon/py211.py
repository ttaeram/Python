import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input().strip())) for _ in range(N)]
def sol(x, y, N):
    first = arr[x][y]
    for r in range(x, x + N):
        for c in range(y, y + N):
            if arr[r][c] != first:
                print('(', end='')
                sol(x, y, N // 2)
                sol(x, (y + N // 2), N // 2)
                sol((x + N // 2), y, N // 2)
                sol((x + N // 2), (y + N // 2), N // 2)
                print(')', end='')
                return
    if arr[x][y] == '1':
        print('1', end='')
    else:
        print('0', end='')
sol(0, 0, N)