import sys
input = sys.stdin.readline

def pick(x, y):
    arr[x][y] = 0
    up_x = x - 1
    if 0 <= up_x < N:
        arr[up_x] = [0] * M

    do_x = x + 1
    if 0 <= do_x < N:
        arr[do_x] = [0] * M
    
    le_y = y - 1
    if 0 <= le_y < M:
        arr[x][le_y] = 0
    
    ri_y = y + 1
    if 0 <= ri_y < M:
        arr[x][ri_y] = 0

while True:
    N, M = map(int, input().split())
    if M == 0 and N == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]
    pick(N//2, M//2)
    print(arr)