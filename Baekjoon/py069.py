N = []

for n in range(9):
    N.append(list(map(int, input().split())))

max_nums = []
for n in N:
    max_nums.append(max(n))

max_num = max(max_nums)
num1 = max_nums.index(max_num) + 1
num2 = N[num1 - 1].index(max_num) + 1
print(max_num)
print(num1, num2)