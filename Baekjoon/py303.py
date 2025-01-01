import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
rra = arr[::-1]

inc = [1] * N
dec = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j] + 1)
        
        if rra[i] >rra[j]:
            dec[i] = max(dec[i], dec[j] + 1)

ans = 0

for n in range(N):
    ans = max(ans, inc[n] + dec[N-n-1] - 1)

print(ans)