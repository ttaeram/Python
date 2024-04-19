from collections import deque
import sys
input = sys.stdin.readline

S = list(map(str, input().strip()))
T = list(map(str, input().strip()))
L = len(T)
S = deque(S)
T = deque(T)
print(S)
def AB(S, L, flag):
    global ans
    if len(S) == L:
        if S == T or S == T[::-1]:
            ans = 1
        return
    if not flag:
        nS = S.appendleft('A')
    else:
        nS = S.append('A')
    AB(nS, L, flag)
    if flag:
        flag = False
        nS = S.append('B')
    else:
        flag = True
        nS = S.appendleft('B')
    AB(nS, L, flag)
    
flag = True
ans = 0
# AB(S, L, flag)
print(ans)