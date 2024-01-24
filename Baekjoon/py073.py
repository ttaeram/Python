N, B = map(int, input().split())

answer = ''

while N != 0:
    a = N % B
    if a >= 10:
        answer += chr(a + 55)
    else:
        answer += str(a)
    N //= B

print(answer[::-1])
# N, B = map(int, input().split())

# alphabet = {}
# for i in range(65, 91):
#     alphabet[i - 55] = chr(i)

# num = []
# while True:
#     if N > B:
#         num.append(N % B)
#         N = N // B
#     elif N < B:
#         num.append(N)
#         break

# for _ in num[::-1]:
#     print(alphabet[_], end = '')