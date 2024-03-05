N = int(input())
arr = list(map(int, input().split()))
first = 0
res = []
while len(res) < N:
    res.append(first % N + 1)
    c = arr[first]
    arr.remove(c)
    first = (first + c) % N
print(arr)
print(res)