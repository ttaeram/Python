import sys
input = sys.stdin.readline
N = int(input())
stack = []
for n in range(N):
    command = input().strip()
    if command[0] == '1':
        stack.append(command[2:])
    
    elif command[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif command[0] == '3':
        print(len(stack))
    
    elif command[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    
    elif command[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)