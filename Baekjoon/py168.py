N = int(input())

res = []
for n in range(1, N + 1):
    arr = [N]
    arr.append(n)

    i = 1
    while True:
        num_2 = arr[i - 1] - arr[i]
        if num_2 < 0:
            break
        
        arr.append(num_2)
        i += 1
    
    if len(arr) > len(res):
        res = arr

print(len(res))
print(*res)