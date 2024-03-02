import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0] * (N + 1)
sum_cnt = 0
for k in range(N):
    sum_cnt += arr[k]
    sum_arr[k + 1] += sum_cnt

for m in range(M):
    i, j = map(int, input().split())
    ans = sum_arr[j] - sum_arr[i - 1]
    print(ans)