A = int(input())
B = int(input())
C = int(input())

arr = [0] * 10
result = str(A * B * C)

for num in result:
    arr[int(num)] += 1

for a in arr:
    print(a)