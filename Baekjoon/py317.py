import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
items = list(map(int, input().split()))
arr = []
for _ in range(R):
    a, b, l = map(int, input().split())
    arr.append((a, b, l))

ans = 0

print(arr)
print(items)
print(ans)