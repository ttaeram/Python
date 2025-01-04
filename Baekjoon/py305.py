import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [input().strip() for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

check = set(arr[0][0])
ans = 1

def sol(r, c, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in check:
                nA = arr[nr][nc]
                check.add(nA)
                sol(nr, nc, cnt + 1)
                check.remove(nA)

sol(0, 0, 1)

print(ans)