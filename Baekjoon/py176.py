N, K = map(int, input().split())

res_1 = 1
res_2 = 1
res_3 = 1

for i in range(1, N + 1):
    res_1 *= i

for j in range(1, (N - K) + 1):
    res_2 *= j

for k in range(1, K + 1):
    res_3 *= k

ans = (res_1 // (res_2 * res_3)) % 1000000007
print(ans)