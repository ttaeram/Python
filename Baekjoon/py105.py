N = int(input())

for num in range(1, N + 1):
    number = num
    num_str = str(num)
    for i in num_str:
        number += int(i)
    
    if number == N:
        print(num)
        break
else:
    print(0)