N, M = map(int, input().split())

A_list = []
B_list = []
A_M_list = []
B_M_list = []
for i in range(N):
    A_M_list = list(map(int, input().split()))
    A_list.append(A_M_list)

for j in range(N):
    B_M_list = list(map(int, input().split()))
    B_list.append(B_M_list)

for n in range(N):
    sum_list = [x + y for x, y in zip(A_list[n], B_list[n])]
    for k in sum_list:
        print(k, end=' ')
    print()