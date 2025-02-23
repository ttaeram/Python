import sys
input = sys.stdin.readline

N, R, Q = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for n in range(N - 1):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

info = []

for q in range(Q):
    u = int(input())
    info.append(u)

print(arr, info)