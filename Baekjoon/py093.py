K, N =  map(int, input().split())

LAN = [int(input()) for _ in range(K)]

start = 1
end = max(LAN)
while start <= end:
    num = 0
    middle = (start + end) // 2
    for line in LAN:
        num += line // middle
    if num < N:
        end = middle - 1
    elif num >= N:
        start = middle + 1

print(end)