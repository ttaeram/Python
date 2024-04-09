from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * 100001
time = 0
stack = deque([(N, time)])
while stack:
    pos, time = stack.popleft()
    if arr[pos] == 0:
        if pos == 0:
            stack.append((pos + 1, time + 1))
        elif 50000 < pos < 100000:
            stack.append((pos - 1, time + 1))
            stack.append((pos + 1, time + 1))
        elif pos == 100000:
            stack.append((pos - 1, time + 1))
        else:
            stack.append((pos - 1, time + 1))
            stack.append((pos + 1, time + 1))
            stack.append((2 * pos, time + 1))
        if pos == K:
            ans = time
            break
        arr[pos] = time
print(ans)
