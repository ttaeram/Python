import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for m in range(M):
    a, b, t = map(int, input().split())
    arr[a].append((b, t))
