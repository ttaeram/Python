N = int(input())
arr = []
x = []
y = []
res = []

for _ in range(6):
    a, b = map(int, input().split())
    arr.append([a, b])
    if a == 1 or a == 2:
        x.append(b)
    if a == 3 or a == 4:
        y.append(b)

for i in range(6):
    if arr[i][0] == arr[(i+2)%6][0]:
        res.append(arr[(i + 1) % 6][1])

ans = (max(x) * max(y) - res[0] * res[1]) * N

print(ans)
#     a, b = map(int, input().split())
#     arr.append(b)

# if arr[0] + arr[2] == arr[4] and arr[1] + arr[3] == arr[5]:
#     ans = (arr[4] * arr[5] - arr[1] * arr[2]) * N

# if arr[1] + arr[3] == arr[5] and arr[2] + arr[4] == arr[0]:
#     ans = (arr[5] * arr[0] - arr[2] * arr[3]) * N

# if arr[2] + arr[4] == arr[0] and arr[3] + arr[5] == arr[1]:
#     ans = (arr[0] * arr[1] - arr[3] * arr[4]) * N

# if arr[3] + arr[5] == arr[1] and arr[4] + arr[0] == arr[2]:
#     ans = (arr[1] * arr[2] - arr[4] * arr[5]) * N

# if arr[4] + arr[0] == arr[2] and arr[5] + arr[1] == arr[3]:
#     ans = (arr[2] * arr[3] - arr[5] * arr[0]) * N

# if arr[5] + arr[1] == arr[3] and arr[0] + arr[4] == arr[4]:
#     ans = (arr[3] * arr[4] - arr[0] * arr[1]) * N
