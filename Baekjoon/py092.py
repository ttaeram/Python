N, K = map(int, input().split())

a = [0, 0] + [1]*(N - 1)
primes=[]

cnt = 0
for i in range(2, N + 1):
  if a[i]:
    primes.append(i)
    for j in range(i, N + 1, i):
        if a[j] == 1:
            a[j] = 0
            cnt += 1
        if cnt == K:
           print(j)
           break