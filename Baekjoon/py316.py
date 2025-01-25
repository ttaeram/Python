import sys
input = sys.stdin.readline

N = int(input())
As = list(map(int, input().split()))
M = int(input())
Bs = list(map(int, input().split()))

def sol(As, Bs, res):
    if (not As) or (not Bs):
        return res
    
    a1, b1 = max(As), max(Bs)
    idxa, idxb = As.index(a1), Bs.index(b1)

    if a1 == b1:
        res.append(a1)
        return sol(As[idxa + 1:], Bs[idxb + 1:], res)
    
    elif a1 > b1:
        As.pop(idxa)
        return sol(As, Bs, res)
    
    else:
        Bs.pop(idxb)
        return sol(As, Bs, res)

ans = sol(As, Bs, [])

print(len(ans))
if ans:
    print(*ans)