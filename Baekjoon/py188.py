from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
check = [0] * (N + 1)
res = [0] * (N + 1)

check[1] = 1
stack = deque([1])
while stack:
    pos = stack.pop()
    for j in arr[pos]:
        if not check[j]:
            stack.append(j)
            check[j] = 1
            res[j] = pos
for k in range(2, N + 1):
    print(res[k])