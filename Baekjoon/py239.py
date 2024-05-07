import sys
input = sys.stdin.readline

A, B = map(int, input().split())

ans = 1
while B != A:
    ans += 1
    res = B
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    
    if res == B:
        print(-1)
        break
else:
    print(ans)


# arr = [B] * (B + 1)
# arr[A] = 1
# for i in range(A, B + 1):
#     i_s = str(i)
#     if int(i_s + '1') <= B:
#         arr[int(i_s + '1')] = min((arr[i] + 1), arr[int(i_s + '1')])
#     if i * 2 <= B:
#         arr[i * 2] = min((arr[i] + 1), arr[i * 2])
# if arr[B] == B:
#     print(-1)
# else:
#     print(arr[B])