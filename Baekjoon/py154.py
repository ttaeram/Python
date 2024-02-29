T = int(input())
for t in range(T):
    N = int(input())
    if N == 0:
        ans = [1, 0]
    elif N == 1:
        ans = [0, 1]
    else:
        arr = [[1, 0], [0, 1]]
        for i in range(2, N + 1):
            arr.append([arr[i - 1][0] + arr[i - 2][0], arr[i - 1][1] + arr[i - 2][1]])
        ans = arr[N]
    print(*ans)