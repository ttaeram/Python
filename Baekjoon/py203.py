import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr_1 = [input().strip() for _ in range(N)]
arr_2 = [input().strip() for _ in range(N)]

ans = 'Eyfa'
for i in range(N):
    res = ''
    for a in arr_1[i]:
        res += a * 2
    if res != arr_2[i]:
        ans = 'Not Eyfa'

print(ans)