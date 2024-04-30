import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(R)]

check = [[0] * C for _ in range(R)]

for r in range(R):
    for c in range(C):
        if arr[r][c] == '.':
            

print(arr)