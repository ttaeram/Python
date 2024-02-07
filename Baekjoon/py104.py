N = int(input())
nums = [int(input()) for _ in range(N)]
stack = []
flag = True
number = 1
plus_minus = []

for n in nums:
    while number <= n:
        stack.append(number)
        plus_minus.append('+')
        number += 1
    
    if stack[-1] == n:
        stack.pop()
        plus_minus.append('-')

    else:
        print('NO')
        flag = False
        break

if flag == True:
    for pl in plus_minus:
        print(pl)