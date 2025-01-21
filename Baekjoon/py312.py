import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

def sol():
    if N == 1:
        return arr[0]
    
    for i in range(1, N):
        arr[i] = max(arr[i], arr[i] + arr[i - 1])
    
    return max(arr)

ans = sol()
print(ans)
