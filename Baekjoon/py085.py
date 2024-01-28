N = int(input())

num_list =list(map(int, input().split()))

num_cnt = 0
for num in num_list:
    cnt = 0
    if num == 1:
        continue
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        num_cnt += 1

print(num_cnt)