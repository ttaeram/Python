import sys
input = sys.stdin.readline

N = int(input())
arr = []
for n in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key = lambda x: (x[1], x[0]))
stack = []
cnt = 0
for i in arr:
    if not stack:
        stack.append(i)
        cnt += 1
    else:
        if stack[-1][1] <= i[0]:
            stack.append(i)
            cnt += 1

print(cnt)