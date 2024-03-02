T = int(input())
for t in range(T):
    closet = {}
    N = int(input())
    for n in range(N):
        a, b = map(str, input().split())
        if b in closet:
            closet[b] += 1
        elif b not in closet:
            closet[b] = 2
    total = 1
    for i in closet.values():
        total *= i
    ans = total - 1
    print(ans)