import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = int(1e6)
idx_1, idx_2 = 0, 0
res = arr[0]

def sol(cnt, idx_1, idx_2, res):
    while True:
        if res >= S:
            cnt = min(cnt, idx_2 - idx_1 + 1)
            res -= arr[idx_1]
            idx_1 += 1
            if idx_1 > idx_2:
                return cnt
        else:
            idx_2 += 1
            if idx_2 < N:
                res += arr[idx_2]
            else:
                return cnt

ans = sol(cnt, idx_1, idx_2, res)
if ans == cnt:
    print(0)
else:
    print(ans)