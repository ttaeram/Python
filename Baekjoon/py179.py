def check(n):
    cnt = 0
    while n >= 5:
        n //= 5
        cnt += n
    return cnt

M = int(input().rstrip())

start = 0
end = 10 ** 9 + 1
res = -1
while start <= end:
    mid = (start + end) // 2
    cnt = check(mid)
    if cnt < M:
        start = mid + 1
    elif cnt == M:
        res = mid
        end = mid - 1
    else:
        end = mid - 1

print(res)