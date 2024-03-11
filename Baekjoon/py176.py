def pe(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    
    res = pe(a, b // 2)
    if b % 2 == 1:
        return res * res * a % p
    else:
        return res * res % p

N, K = map(int, input().split())
p = 1000000007

res_1 = 1
res_2 = 1

for i in range(1, N + 1):
    res_1 = (res_1 * i) % p

for j in range(1, (N - K) + 1):
    res_2 = (res_2 * j) % p

for k in range(1, K + 1):
    res_2 = (res_2 * k) % p

ans = (res_1 * pe(res_2, p - 2)) % p
print(ans)