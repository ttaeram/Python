import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
while end >= start:
    mid = (start + end) // 2
    res = 0
    for a in arr:
        if a > mid:
            ch = a - mid
            res += ch
    if res >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)