arr = [1, 2, 3, 4]
check = [0 for _ in range(len(arr))]

def comb(chosen, check):
    if len(chosen) == 4:
        print(chosen)
        return

    for i in range(len(arr)):
        if not check[i]:
            chosen.append(arr[i])
            check[i] = 1
            comb(chosen, check)
            check[i] = 0
            chosen.pop()
comb([], check)