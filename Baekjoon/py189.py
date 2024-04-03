import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# egg = 0
# next = 1
# while True:
#     if egg == N - 1:
#         break
#     arr[egg] = [arr[egg][0] - arr[egg + next][1], arr[egg][1]]
#     arr[egg + next] = [arr[egg + next][0] - arr[egg][1], arr[egg + next][1]]
#     if egg + next < N and arr[egg + next][0] <= 0:
#         arr[egg + next] = [0, 0]
#         next += 1
#     if arr[egg][0] <= 0:
#         egg += 1
#         next = 1
# print(arr)

def breaking(n):
    if n == N:
        cnt = 0
        for i in range(N):
            if arr[i][0] <= 0:
                cnt += 1
        return cnt
    
    if arr[n][0] <= 0:
        return breaking(n + 1)
    for j in range(N):
        if j == n:
            continue
        if arr[j][0] > 0:
            break
    else:
        return breaking(n + 1)
    ans = 0
    for k in range(N):
        if k == n:
            continue
        if arr[k][0] <= 0:
            continue
        arr[k][0] -= arr[n][1]
        arr[n][0] -= arr[k][1]

        ans = max(ans, breaking(n + 1))

        arr[k][0] += arr[n][1]
        arr[n][0] += arr[k][1]
    return ans

print(breaking(0))