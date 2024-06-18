import sys
input = sys.stdin.readline
R, C, T = map(int, input().split())
arr = []
gong = []
for r in range(R):
    arr_ = list(map(int, input().split()))
    arr.append(arr_)
    for c in range(C):
        if arr[r][c] == -1:
            gong.append((r, c))

def hwak():
    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]
    arr_hwak = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c] != 0 and arr[r][c] != -1:
                res = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                        arr_hwak[nr][nc] += arr[r][c] // 5
                        res += arr[r][c] // 5
                arr[r][c] -= res
    for r in range(R):
        for c in range(C):
            arr[r][c] += arr_hwak[r][c]

def gong_top():
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    d = 0
    pre = 0
    r, c = gong[0][0], 1
    while True:
        nr = r + dr[d]
        nc = c + dc[d]
        if (r, c) == gong[0]:
            break
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            d += 1
            continue
        arr[r][c], pre = pre, arr[r][c]
        r, c = nr, nc

def gong_bot():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    pre = 0
    r, c = gong[1][0], 1
    while True:
        nr = r + dr[d]
        nc = c + dc[d]
        if (r, c) == gong[1]:
            break
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            d += 1
            continue
        arr[r][c], pre = pre, arr[r][c]
        r, c = nr, nc

def sol():
    for t in range(T):
        hwak()
        gong_top()
        gong_bot()
    
    ans = 0
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                ans += arr[r][c]
    return ans

ans = sol()
print(ans)