import sys
input = sys.stdin.readline

N = int(input())
res = ''
for n in range(N):
    S, T = map(str, input().split())
    for i in range(len(S)):
        if S[i] == 'x' or S[i] == 'X':
            if T[i].isalpha():
                print(T[i].upper(),end = '')
            else:
                print(T[i],end = '')