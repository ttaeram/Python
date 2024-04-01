from collections import deque
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
arr = list(map(int, input().split()))
arr = deque(arr)
bridge = [0] * w
bridge = deque(bridge)
on = 0
cnt = 0
while bridge:
    out = bridge.popleft()
    on -= out
    if arr:
        if on + arr[0] <= L:
            truck = arr.popleft()
            bridge.append(truck)
            on += truck
        else:
            bridge.append(0)
    cnt += 1
        
print(cnt)