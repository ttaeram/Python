import sys
input = sys.stdin.readline

arr = []
N = int(input())
for n in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key = lambda x: (x[1], x[0]))

for i in arr:
    print(*i)