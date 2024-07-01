import sys
input = sys.stdin.readline

N, M = map(int, input().split())
check = [int(input()) for _ in range(N)]

left = min(check)
right = max(check) * M
ans = right

while left <= right:
    mid = (left + right) // 2
    res = 0
    for c in check:
        res += (mid // c)
    
    if res >= M:
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)