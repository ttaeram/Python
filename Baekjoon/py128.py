N, K = map(int, input().split())

N_ = 1
for n in range(1, N + 1):
    N_ *= n

K_ = 1
for k in range(1, K + 1):
    K_ *= k

NK_ = 1
for nk in range(1, N - K + 1):
    NK_ *= nk

result = N_ // (NK_ * K_)
print(result)