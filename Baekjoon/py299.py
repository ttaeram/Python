import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())

ladder = {}
def bridging(a, b):
    if b in ladder:
        ladder[b].append((a, b+1))
    else:
        ladder[a] = [(a, b+1)]
    
    if b+1 in ladder:
        ladder[b+1].append((a, b))
    else:
        ladder[b+1] = [(a, b)]

def down(i):
    sero = i
    garo = 0
    while garo < H:
        for a, b in ladder[sero]:
            if a == garo:
                sero = b
                break
        garo += 1
    
    if sero == i:
        return True
    else:
        return False
    
def sol():
    global ans
    

for _ in range(M):
    a, b = map(int, input().split())
    bridging(a-1, b-1)

ans = 0

for n in range(N):
    print(down(n))
