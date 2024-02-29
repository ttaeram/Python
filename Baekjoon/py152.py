import sys
input = sys.stdin.readline

N = int(input())
S = set()
for n in range(N):
    command = input().strip()
    if 'add' in command:
        a, b = map(str, command.split())
        S.add(int(b))
    
    elif 'remove' in command:
        a, b = map(str, command.split())
        if int(b) in S:
            S.discard(int(b))
    
    elif 'check' in command:
        a, b = map(str, command.split())
        if int(b) in S:
            print(1)
        else:
            print(0)
    
    elif 'toggle' in command:
        a, b = map(str, command.split())
        if int(b) in S:
            S.discard(int(b))
        else:
            S.add(int(b))
    
    elif command == 'all':
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

    elif command == 'empty':
        S = set()