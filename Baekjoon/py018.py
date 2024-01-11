H, M = map(int, input().split())

if H == 0 and M < 45:
    H = 23
    M += 15
    print(H ,M)
elif M < 45:
    H -= 1
    M += 15
    print(H ,M)
else:
    M -= 45
    print(H, M)