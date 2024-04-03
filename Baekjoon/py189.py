import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
egg = 0
next = 1
while True:
    if egg == N - 1:
        break
    arr[egg] = [arr[egg][0] - arr[egg + next][1], arr[egg][1]]
    arr[egg + next] = [arr[egg + next][0] - arr[egg][1], arr[egg + next][1]]
    if egg + next < N and arr[egg + next][0] <= 0:
        arr[egg + next] = [0, 0]
        next += 1
    if arr[egg][0] <= 0:
        egg += 1
        next = 1
print(arr)