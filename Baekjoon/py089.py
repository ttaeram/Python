N = int(input())

fact = 1
for i in range(1, N + 1):   # N의 팩토리얼 구하기
    fact *= i

num_0 = 0
fact = str(fact)
fact_rev = fact[::-1]

for num in fact_rev:
    if num == '0':
        num_0 += 1
    if num != '0':
        break
print(num_0)