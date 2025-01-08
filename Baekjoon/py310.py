import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = ['0']

for _ in range(N):
    inp = input().strip()
    arr.append('0' + inp)

res = [[0] * (M + 1) for _ in range(N + 1)]

def init():
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            res[r][c] = res[r - 1][c] + res[r][c - 1] - res[r - 1][c - 1] + int(arr[r][c])

def calculate(r1, c1, r2, c2):
    return res[r2][c2] - res[r2][c1 - 1] - res[r1 - 1][c2] + res[r1 - 1][c1 - 1]

def sol():
    ans = 0

    for r in range(1, M - 1):
        for c in range(r + 1, M):
            r1 = calculate(1, 1, N, r)
            r2 = calculate(1, r + 1, N, c)
            r3 = calculate(1, c + 1, N, M)

            sna = r1 * r2 * r3

            if ans < sna:
                ans = sna
    
    for r in range(1, N - 1):
        for c in range(r + 1, N):
            r1 = calculate(1, 1, r, M)
            r2 = calculate(r + 1, 1, c, M)
            r3 = calculate(c + 1, 1, N, M)

            sna = r1 * r2 * r3

            if ans < sna:
                ans = sna
    
    for r in range(1, M):
        for c in range(1, N):
            r1 = calculate(1, 1, N, r)
            r2 = calculate(1, r + 1, c, M)
            r3 = calculate(c + 1, r + 1, N, M)

            sna = r1 * r2 * r3

            if ans < sna:
                ans = sna
    
    for r in range(1, N):
        for c in range(1, M):
            r1 = calculate(1, 1, r, c)
            r2 = calculate(r + 1, 1, N, c)
            r3 = calculate(1, c + 1, N, M)

            sna = r1 * r2 * r3

            if ans < sna:
                ans = sna
    
    for r in range(1, N):
        for c in range(1, M):
            r1 = calculate(1, 1, r, M)
            r2 = calculate(r + 1, 1, N, c)
            r3 = calculate(r + 1, c + 1, N, M)

            sna = r1 * r2 * r3

            if ans < sna:
                ans = sna
    
    for r in range(1, N):
        for c in range(1, M):
            r1 = calculate(1, 1, r, c)
            r2 = calculate(1, c + 1, r, M)
            r3 = calculate(r + 1, 1, N, M)

            sna = r1 * r2 * r3

            if ans < sna:
                ans = sna
    
    return ans

init()
ans = sol()
print(ans)