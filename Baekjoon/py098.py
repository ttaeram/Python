arr = list(map(int, input().split()))

total = 0
for a in arr:
    total += a ** 2

result = total % 10
print(result)