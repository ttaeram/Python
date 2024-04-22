import sys
input = sys.stdin.readline

N, D = map(int, input().split())

Ji = []
for n in range(N):
    a, b, c = map(int, input().split())
    Ji.append((a, b, c))

path = [0] * (D + 1)

for i in range(1, D + 1):
    path[i] = path[i - 1] + 1
    for n in range(N):
        s, e, d = Ji[n]
        if e == i:
            path[e] = min(path[e], path[s] + d)
    
print(path[D])