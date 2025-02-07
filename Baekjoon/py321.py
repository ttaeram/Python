import sys
input = sys.stdin.readline

N = int(input())
arr = [[" "] * 2 * N for _ in range(N)]

def sol(i, j, phase):
    if phase == 3:
        arr[i][j] = "*"
        arr[i + 1][j - 1] = "*"
        arr[i + 1][j + 1] = "*"

        for k in range(-2, 3):
            arr[i + 2][j - k] = "*"
        
    else:
        newPhase = phase // 2
        sol(i, j, newPhase)
        sol(i + newPhase, j - newPhase, newPhase)
        sol(i + newPhase, j + newPhase, newPhase)

sol(0, N - 1, N)

for ans in arr:
    print("".join(ans))