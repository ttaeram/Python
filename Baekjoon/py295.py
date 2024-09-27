from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]

dx = [0, 1]
dy = [1, 0]

results = []

def sol():
    dq = deque([(0, 0)])
    com = []
    while dq:
        x, y = dq.pop()
        com = com[:(x+y)]
        com.append(arr[x][y])
        if len(com) == 2*N-1:
            cal(com)
        
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                dq.append((nx, ny))

def cal(com):
    res = int(com[0])
    for n in range(1, len(com), 2):
        if com[n] == '*':
            res *= int(com[n+1])
        elif com[n] == '+':
            res += int(com[n+1])
        else:
            res -= int(com[n+1])
    
    results.append(res)


sol()
min_ans = min(results)
max_ans = max(results)
print(max_ans, min_ans)