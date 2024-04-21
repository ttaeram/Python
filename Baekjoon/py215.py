from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    command = input().strip()
    N = int(input())
    inp = input().strip()
    arr = []
    if N > 0:
        num = ''
        for i in range(len(inp)):
            if inp[i].isnumeric():
                num += inp[i]
            elif inp[i] == ']':
                arr.append(int(num))
            elif inp[i] == ',':
                arr.append(int(num))
                num = ''
    else:
        arr = []
    arr = deque(arr)
    flag = 1
    cont = True
    for i in range(len(command)):
        if command[i] == 'R':
            flag *= -1
        elif command[i] == 'D':
            if arr:
                if flag == 1:
                    arr.popleft()
                elif flag == -1:
                    arr.pop()
            else:
                print('error')
                cont = False
                break
    if flag == -1:
        arr.reverse()
    if not cont:
        continue
    else:
        print('[', end='')
        for i in range(len(arr)):
            if i == len(arr) - 1:
                print(arr[i], end='')
            else:
                print(arr[i], end=',')
        print(']')