import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * N for _ in range(N)]

def sol(n):
    global N, cnt

    if n == N:
        cnt += 1
        return
    
    for i in range(N):
        if not check_c[i] and not check_xp[n + i] and not check_xd[(N - 1) + n - i]:
            check_c[i] = 1
            check_xp[n + i] = 1
            check_xd[(N - 1) + n - i] = 1
            sol(n + 1)
            check_c[i] = 0
            check_xp[n + i] = 0
            check_xd[(N - 1) + n - i] = 0

check_c = [0] * N
check_xp = [0] * (2 * (N - 1) + 1)
check_xd = [0] * (2 * (N - 1) + 1)
cnt = 0

sol(0)

print(cnt)