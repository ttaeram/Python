import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for r in range(1, N):
    for c in range(len(arr[r])):
        if c == 0:
            arr[r][c] += arr[r - 1][c]
        elif c == len(arr[r]) - 1:
            arr[r][c] += arr[r - 1][c - 1]
        else:
            arr[r][c] = max((arr[r][c] + arr[r - 1][c - 1]), (arr[r][c] + arr[r - 1][c]))

ans = max(arr[N-1])
print(ans)