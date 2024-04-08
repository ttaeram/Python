import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

S = sum(arr)
total = S // M
tottt = S // (M - 1)

max_res = 0
res = 0
for n in arr:
    res += n
    if total <= res < tottt:
        max_res = max(res, max_res)
        res = 0
    if total >= tottt:
        res -= n
        max_res = max(res, max_res)
        res = n

ans = max_res
print(ans)
