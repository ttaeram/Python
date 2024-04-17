from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for m in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

answer = []
for i in range(1, N + 1):
    res = 0
    for j in range(1, N + 1):
        if i != j:
            check = [0] * (N + 1)
            stack = deque([(i, 0)])
            flag = True
            while stack:
                pos, d = stack.popleft()
                if check[pos] == 0:
                    check[pos] = 1
                    for k in arr[pos]:
                        if k == j:
                            res += (d + 1)
                            flag = False
                            break
                        stack.append((k, d + 1))
                    if not flag:
                        break
    answer.append((res, i))
answer.sort()
ans = answer[0][1]
print(ans)
