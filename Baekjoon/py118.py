import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    k = int(input())
    n = int(input())

    apartment = [[0] * n for _ in range(k + 1)]

    for i in range(1, n + 1):
        apartment[0][i - 1] = i
    
    for j in range(1, k + 1):
        apartment[j][0] = apartment[j - 1][0]
    
    for h in range(1, k):
        for f in range(n):
            if n == 0:
                apartment[h][n] = apartment[h - 1][n]
            else:
                apartment[h][n] += apartment[h - 1][n - 1]
    print(apartment)