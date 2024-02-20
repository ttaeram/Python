from collections import deque

N, K = map(int, input().split())

arr = deque()
for n in range(1, N + 1):
    arr.append(n)

res = []
while len(arr) != 0:
    for k in range(K - 1):
        arr.append(arr.popleft())
    
    res.append(str(arr.popleft()))

print('<' + ', '.join(res) + '>')