N = int(input())

result = 0
m = 
while m < N:
    number = m
    M = str(m)
    for i in M:
        num = int(i)
        number += num
    if number == N:
        result = number
        break
    elif number != N: 
        m += 1
        number = 0
print(result)