import sys
input = sys.stdin.readline

N, K = map(int, input().split())
if N >= K:
    ans = N - K
    print(ans)

else:
    arr = [0] * (K + 2)
    for i in range(N, K + 2):
        if i & 2 == 0:
            if N <= i <= K+1:
                arr[i] = min(arr[i-1] + 1, arr[i+1] + 1, arr[i//2])
            else:
                arr[i] = min(arr[i-1] + 1, arr[i+1] + 1)
        else:
            arr[i] = min(arr[i-1] + 1, arr[i+1] + 1)

print(arr[K])