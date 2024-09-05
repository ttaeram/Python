import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

def check(mid):
    max_n, min_n = arr[0], arr[0]
    cnt = 1

    for n in range(1, N):
        max_n = max(max_n, arr[n])
        min_n = min(min_n, arr[n])

        if max_n - min_n > mid:
            cnt += 1
            max_n, min_n = arr[n], arr[n]
    
    return cnt

def sol():
    start, end = 0, max(arr)
    ans = 0
    
    while start <= end:
        mid = (start + end) // 2
        res = check(mid)

        if res <= M:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1

    return ans

ans = sol()
print(ans)