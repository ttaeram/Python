A, B = map(int, input().split())

for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        min_p = i

max_p = (A // min_p) * B
print(min_p)
print(max_p)