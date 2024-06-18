import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [[0] * 201 for _ in range(201)]
def sol():
    for i in range(201):
        arr[1][i] = 1
        arr[2][i] = i + 1

    for i in range(2, 201):
        arr[i][1] = i
        for j in range(2, 201):
            arr[i][j] = (arr[i][j - 1] + arr[i - 1][j]) % 1000000000
sol()
ans = arr[K][N]
print(ans)