N, M = map(int, input().split())
basket = list(range(1, N + 1))

for n in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for a in basket:
    print(a, end = ' ')