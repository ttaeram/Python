from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

mapp = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            mapp[i][j] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    mapp[a][b] = min(c, mapp[a][b])

def sol():
    for i in range(1, N + 1):
        for r in range(1, N + 1):
            for c in range(1, N + 1):
                mapp[r][c] = min(mapp[r][c], mapp[r][i] + mapp[i][c])

    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if mapp[r][c] == int(1e9):
                print("0", end =" ")
            
            else:
                print(mapp[r][c], end = " ")
        
        print()

sol()