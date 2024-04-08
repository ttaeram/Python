import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

end = sum(arr)
start = max(arr)
ans = end

while start <= end:
    mid = (start + end) // 2
    total = 0
    cnt = 1
    for n in arr:
        if total + n > mid:
            cnt += 1
            total = 0
        total += n

    if cnt == M:
        ans = mid
        end = mid - 1
    elif cnt > M:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)