import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

def AB(S, T):
    global ans
    if len(S) == len(T):
        if S == T:
            ans = 1
        return
    if T[-1] == 'A':
        AB(S, T[:-1])
    if T[0] == 'B':
        AB(S, T[:0:-1])
    
ans = 0
AB(S, T)
print(ans)