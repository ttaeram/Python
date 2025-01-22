import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input().strip()) for _ in range(N)]
cnt = [0] * (K + 1)
cnt[0] = 1

def sol():
    for coin in arr:
        for tar in range(coin, K+1):
            
            if tar - coin >= 0:
                cnt[tar] += cnt[tar - coin]
    
sol()
ans = cnt[K]
print(ans)