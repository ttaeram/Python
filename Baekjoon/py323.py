import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def multiple(U, V):
    n = len(U)
    Z = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):

            e = 0
            for i in range(n):
                e += U[r][i] * V[i][c]
            
            Z[r][c] = e % 1000
    
    return Z

def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        
        return A
    
    res = square(A, B // 2)

    if B % 2:
        return multiple(multiple(res, res), A)
    
    else:
        return(multiple(res, res))

answer = square(A, B)

for ans in answer:
    print(*ans)