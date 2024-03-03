N = int(input())
arr = [0, 1]

for i in range(2, N + 1):
    min_v = 2500000001
    j = 1
    while j ** 2 <= i:
        min_v = min(min_v, arr[i - j ** 2])
        j += 1
    arr.append(min_v + 1)

print(arr[N])