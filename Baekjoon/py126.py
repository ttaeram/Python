import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

q = deque()
for n in range(N):
    command = input().rstrip()
    if 'push' in command:
        q.append(int(command[5:]))
    
    elif command == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    
    elif command == 'size':
        print(len(q))
    
    elif command == 'empty':
        if q:
            print(0)
        else:
            print(1)
    
    elif command == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    
    elif command == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)