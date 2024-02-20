N = int(input())

arr = []
for n in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort()

for i in arr:
    print(*i)