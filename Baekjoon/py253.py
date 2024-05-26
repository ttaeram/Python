import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    res = [[0] * N for _ in range(2)]
    if N == 1:
        ans = max(arr[0][0], arr[1][0])
        print(ans)
        continue
    elif N == 2:
        ans = max(arr[0][0] + arr[1][1], arr[0][1] + arr[1][0])
        print(ans)
        continue
    else:
        for n in range(N):
            if n == 0:
                res[0][n] = arr[0][n]
                res[1][n] = arr[1][n]
            elif n == 1:
                res[0][n] = arr[1][n-1] + arr[0][n]
                res[1][n] = arr[0][n-1] + arr[1][n]
            else:
                res[0][n] = max(arr[0][n] + res[1][n - 1], arr[0][n] + res[1][n - 2])
                res[1][n] = max(arr[1][n] + res[0][n - 1], arr[1][n] + res[0][n - 2])
        ans = max(res[0][- 1], res[1][- 1])
        print(ans)