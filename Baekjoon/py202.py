import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
s = 'I'

def sol(N, M, S):
    s = 'I'
    for _ in range(N):
        s += 'OI'
    cnt = 0
    for m in range(M):
        if S[m] == 'O':
            continue
        elif m < M - 1 and S[m] == S[m + 1]:
            continue
        if S[m:m + (2 * N + 1)] == s:
            cnt += 1
    return cnt

ans = sol(N, M, S)
print(ans)