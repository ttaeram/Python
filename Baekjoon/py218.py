from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
command = ['D', 'S', 'L', 'R']
for t in range(T):
    A, B = map(int, input().split())
    stack = deque([(A, '')])
    check = set()
    flag = True
    while True:
        A, com = stack.popleft()
        for c in command:
            AA = A
            comm = com
            if c == 'D':
                AA = 2 * AA
                if AA > 9999:
                    AA = AA % 10000
                if AA == B:
                    ans = comm + 'D'
                    flag = False
                    break
                if AA not in check:
                    stack.append((AA, comm + 'D'))
                    check.add(AA)
            elif c == 'S':
                if AA == 0:
                    AA = 9999
                else:
                    AA = AA - 1
                if AA == B:
                    ans = comm + 'S'
                    flag = False
                    break
                if AA not in check:
                    stack.append((AA, comm + 'S'))
                    check.add(AA)
            elif c == 'L':
                sA = str(AA)
                if len(sA) % 4 != 0:
                    nA = ''
                    for i in range(4 - (len(sA) % 4)):
                        nA += '0'
                    sA = nA + sA
                sA = sA[1:4] + sA[0]
                AA = int(sA)
                if AA == B:
                    ans = comm + 'L'
                    flag = False
                    break
                if AA not in check:
                    stack.append((AA, comm + 'L'))
                    check.add(AA)
            elif c == 'R':
                sA = str(AA)
                if len(sA) % 4 != 0:
                    nA = ''
                    for i in range(4 - (len(sA) % 4)):
                        nA += '0'
                    sA = nA + sA
                sA = sA[3] + sA[0:3]
                AA = int(sA)
                if AA == B:
                    ans = comm + 'R'
                    flag = False
                    break
                if AA not in check:
                    stack.append((AA, comm + 'R'))
                    check.add(AA)
        if not flag:
            break
    print(ans)