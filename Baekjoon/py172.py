from collections import deque
import sys
input = sys.stdin.readline
arr = deque()
N = int(input())
for n in range(N):
    command = input().strip()
    if 'push' in command:
        arr.append(command[5:])
    elif command == 'pop':
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(arr))
    elif command == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif command == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)