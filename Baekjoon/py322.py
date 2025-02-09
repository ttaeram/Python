import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
arr = []

for _ in range(E):
    u, v, w = map(int, input().split())
    arr.append((u, v, w))

print(arr)