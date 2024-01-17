N, M = map(int, input().split())

basket = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = (reversed(basket[i-1:j]))

for _ in range(N):
    print(basket[_], end = ' ')