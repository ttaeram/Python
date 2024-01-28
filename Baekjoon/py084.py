while True:
    N = int(input())
    if N == -1:
        break

    i_list = []
    for i in range(1, N+1):
        if N % i == 0:
            i_list.append(i)
            i_list_sorted = sorted(i_list)

    if sum(i_list_sorted) - i_list_sorted[-1] == N:
        for n in i_list_sorted[:-1]:
            if n == i_list_sorted[0]:
                print(f'{N} = {n} + ', end = '')
            elif n == i_list_sorted[-2]:
                print(f'{n}')
            else:
                print(f'{n} + ', end = '')
    else:
        print(f'{N} is NOT perfect.')