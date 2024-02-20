from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

q = deque()
for n in range(N):
    command = input().rstrip()
    if 'push_front' in command:
        q.appendleft(int(command[11:]))
    
    elif 'push_back' in command:
        q.append(int(command[10:]))
    
    elif command == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif command == 'pop_back':
        if q:
            print(q.pop())
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