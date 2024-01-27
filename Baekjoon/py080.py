num_list = []
while True:
    N = input()
    if int(N) == 0:
        break
    num_list.append(N)

for n in num_list:
    if n[::-1] == n:
        print('yes')
    else:
        print('no')