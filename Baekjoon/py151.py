import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse = True)

cnt = 0
for coin in coins:
    if K // coin != 0:
        c = K // coin
        K -= coin * c
        cnt += c
        if K == 0:
            break
print(cnt)