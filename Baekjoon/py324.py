import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque()
q.append(N)
arr = [0] * 100001
cnt, ans = 0, 0

def sol():
    global ans, cnt
    while q:
        idx = q.popleft()
        res = arr[idx]

        if idx == K:
            ans = res
            cnt += 1
            continue

        for i in [idx - 1, idx + 1, idx * 2]:
            if 0 <= i < 100001 and (arr[i] == 0 or arr[i] == arr[idx] + 1):
                arr[i] = arr[idx] + 1
                q.append(i)

sol()
print(ans)
print(cnt)