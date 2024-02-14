A, B = map(int, input().split())

a = [0, 0] + [1] * (A - 1)
primes_A = []

cnt = 0
for i in range(2, A + 1):
  if a[i]:
    primes_A.append(i)
    for j in range(i, A + 1, i):
        if a[j] == 1:
            a[j] = 0
            cnt += 1
        if cnt == K:
           print(j)
           break