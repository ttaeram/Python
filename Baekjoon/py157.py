N = int(input())
arr = [0] * 1001
if N == 1:
    ans = 1
elif N == 2:
    ans = 2
elif N > 2:
    arr[1] = 1
    arr[2] = 2
    for n in range(3, N + 1):
        arr[n] = arr[n - 1] + arr[n - 2]
    ans = arr[N]
print(ans % 10007)