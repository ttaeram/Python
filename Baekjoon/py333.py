import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

N, R, Q = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for n in range(N - 1):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

check = [0] * (N + 1)

def sol(n):
    global check
    check[n] = 1
    
    for i in arr[n]:
        if check[i] == 0:
            check[n] += sol(i)
    
    return check[n]

sol(R)

for q in range(Q):
    u = int(input())
    print(check[u])