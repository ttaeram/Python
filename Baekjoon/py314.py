import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()

def sol():
    dp = [1] * N

    for i in range(1, N):
        for j in range(i):
            if arr[j][1] < arr[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    ans = N - max(dp)
    return ans

ans = sol()
print(ans)