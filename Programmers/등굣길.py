def solution(m, n, puddles):
    arr = [[0] * m for _ in range(n)]
    oong = set()
    for i in range(len(puddles)):
        a, b = puddles[i][0] - 1, puddles[i][1] - 1
        oong.add((b, a))
    arr[0][0] = 1
    for r in range(n):
        for c in range(m):
            if r == 0 and c == 0:
                continue
            if (r, c) in oong:
                arr[r][c] = 0
            else:
                if r == 0:
                    arr[r][c] = arr[r][c - 1]
                elif c == 0:
                    arr[r][c] = arr[r - 1][c]
                else:
                    arr[r][c] = arr[r][c - 1] + arr[r - 1][c]
    return arr[n - 1][m - 1] % 1000000007

puddles = []
print(solution(100, 100, puddles))