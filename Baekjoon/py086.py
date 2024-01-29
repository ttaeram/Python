M = int(input())
N = int(input())

result_list = []
for num in range(M, N + 1):
    num_list = []
    for n in range(1, num + 1):
        if num % n == 0:
            num_list.append(n)
    if len(num_list) == 2:
        result_list.append(num)

if 1 in result_list:
    result_list.remove(1)
if len(result_list) == 0:
    print(-1)
else:
    total = sum(result_list)
    print(total)
    print(min(result_list))