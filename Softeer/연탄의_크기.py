import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

max_cnt = 0
for j in range(2, 101):
    cnt = 0
    for i in range(N):
        if arr[i] % j == 0:
            cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)