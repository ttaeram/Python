from collections import deque
import sys
input = sys.stdin.readline
 
arr = [list(input().strip()) for _ in range(12)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]
 
cnt = 0
 
while True:
    flag = False
    check = [[0] * 6 for _ in range(12)]
 
    for r in range(12):
        for c in range(6):
            if arr[r][c] != "." and not check[r][c]:
                semi = deque()
                semi.append((r, c))
                check[r][c] = 1
                res = []
                res.append((r, c))

                while semi:
                    r, c = semi.popleft()
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if 0 <= nr < 12 and 0 <= nc < 6 and arr[r][c] == arr[nr][nc]:
                            if not check[nr][nc]:
                                semi.append((nr, nc))
                                check[nr][nc] = 1
                                res.append((nr, nc))
 
                if len(res) >= 4:
                    flag = True
                    for r, c in res:
                        arr[r][c] = '.'
 
    if flag:
        for c in range(6):
            for r in range(10, -1, -1):
                for n in range(11, r, -1):
                    if arr[r][c] != '.' and arr[n][c] == '.':
                        arr[n][c] = arr[r][c]
                        arr[r][c] = '.'
        cnt += 1
    else:
        break

print(cnt)