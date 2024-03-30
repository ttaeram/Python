import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(str, input().strip().split()))
    ans = int(1e9)
    if N > 32:
        ans = 0
        print(ans)
        continue
    for i in range(N):
        for j in range(N):
            for k in range(N):
                cnt = 0
                if i == j or j == k or k == i:
                    continue
                for l in range(4):
                    if arr[i][l] != arr[j][l]:
                        cnt += 1
                    if arr[i][l] != arr[k][l]:
                        cnt += 1
                    if arr[j][l] != arr[k][l]:
                        cnt += 1
                ans = min(cnt, ans)
    print(ans)