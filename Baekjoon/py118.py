import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    k = int(input())    # 층
    n = int(input())    # 방

    apartment = [num for num in range(1, n + 1)]

    for i in range(k):
        for j in range(1, n):
            apartment[j] += apartment[j - 1]
        
    
    print(apartment[-1])

    # apartment = [[0] * n for _ in range(k + 1)]

    # for i in range(1, n + 1):
    #     apartment[0][i - 1] = i
    
    # for j in range(1, k):
    #     for l in range(1, n):
    #         apartment[j][l] += apartment[j - 1][l - 1]
    # print(apartment)