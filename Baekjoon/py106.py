from collections import deque

N = int(input())
arr = deque()
arr = deque(range(1, N + 1))

while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())
    
print(*arr)
# arr = list(range(1, N + 1))

# while len(arr) > 1:
#     arr.pop(0)
#     arr.append(arr.pop(0))

# print(*arr)