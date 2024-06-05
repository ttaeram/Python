import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N, M = map(int, input().split())
jip = {}
for i in range(N + 1):
    jip[i] = i

def one(i):
    if jip[i] != i:
        jip[i] = one(jip[i])
    return jip[i]

def zero(a, b):
    ai = one(a)
    bi = one(b)
    if ai < bi:
        jip[bi] = ai
    else:
        jip[ai] = bi

def sol():
    for m in range(M):
        c, a, b = map(int, input().split())
        if c == 0:
            zero(a, b)

        elif c == 1:
            ai = one(a)
            bi = one(b)
            if ai == bi:
                print('YES')
            else:
                print('NO')
sol()