from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
stack = deque()
for n in range(N):
    command = input().strip()
    if command[0] == '1':
        stack.appendleft(command[2:])

    elif command[0] == '2':
        stack.append(command[2:])
    
    elif command[0] == '3':
        if stack:
            print(stack.popleft())
        else:
            print(-1)

    elif command[0] == '4':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif command[0] == '5':
        print(len(stack))
    
    elif command[0] == '6':
        if stack:
            print(0)
        else:
            print(1)
    
    elif command[0] == '7':
        if stack:
            print(stack[0])
        else:
            print(-1)

    elif command[0] == '8':
        if stack:
            print(stack[-1])
        else:
            print(-1)