N = int(input())

if N % 5 == 0:
    ans = -1
else:
    ans = 5 * (N - N // 5)

print(ans)