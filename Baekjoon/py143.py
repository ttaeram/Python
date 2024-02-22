N = int(input())

arr = [0] * (N + 1)
for i in range(2, N + 1):
    min_cnt = 1000001
    if i % 3 == 0:
        if i % 2 == 0:
            min_cnt = min(arr[i // 3], arr[i // 2], arr[i - 1])
            arr[i] = min_cnt + 1
        else:
            min_cnt = min(arr[i // 3], arr[i - 1])
            arr[i] = min_cnt + 1
    elif i % 2 == 0:
        min_cnt = min(arr[i // 2], arr[i - 1])
        arr[i] = min_cnt + 1
    else:
        min_cnt = arr[i - 1]
        arr[i] = min_cnt + 1

print(arr[N])