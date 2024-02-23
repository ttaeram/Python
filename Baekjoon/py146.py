N = int(input())
arr = []
for _ in range(6):
    a, b = map(int, input().split())
    arr.append(b)

if arr[0] + arr[2] == arr[4] and arr[1] + arr[3] == arr[5]:
    ans = (arr[4] * arr[5] - arr[1] * arr[2]) * N

elif arr[1] + arr[3] == arr[5] and arr[2] + arr[4] == arr[0]:
    ans = (arr[0] * arr[5] - arr[2] * arr[3]) * N

elif arr[2] + arr[4] == arr[0] and arr[3] + arr[5] == arr[1]:
    ans = (arr[0] * arr[1] - arr[3] * arr[4]) * N

print(ans)