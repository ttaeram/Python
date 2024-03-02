T = int(input())
arr = [0, 1, 1, 1, 2, 2] + [0] * 95
for t in range(T):
    N = int(input())
    if N > 5:
        for n in range(6, N + 1):
            arr[n] = arr[n - 1] + arr[n - 5]
    ans = arr[N]
    print(ans)