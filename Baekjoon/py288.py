import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

def sol():
    res = 0
    for i in range(N):
        now = arr[i]
        if i % 2 == 0:
            res += arr[i]
    
    ans = res
    semi = res
    for j in range(N-1, 0, -2):
        semi += arr[j]
        semi -= arr[j-1]
        ans = max(ans, semi)

    semi = res
    for j in range(N-2, 1, -2):
        semi -= arr[j]
        semi += arr[j-1]
        ans = max(ans, semi)

    return ans

ans = sol()
print(ans)
