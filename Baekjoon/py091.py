M, N = map(int, input().split())

a = [0, 0] + [1] * (N - 1)
primes = []

for i in range(2, N + 1):
    if a[i] == 1:
        # primes.append(i)
        if i >= M:
            print(i)
        for j in range(i * 2, N + 1, i):
            a[j] = 0
# for i in range(M, N + 1):
#     i_list = []
#     for j in range(1, i + 1):
#         if i % j == 0:
#             i_list.append(j)
#     if len(i_list) == 2:
#         print(i_list[1])