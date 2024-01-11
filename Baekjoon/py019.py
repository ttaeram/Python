H, M = map(int, input().split())
T = int(input())

if M + T >= 60:
    H = (H + (M + T)//60) % 24
    M = (M + T) % 60
    print(H ,M)
else:
    H = H % 24
    M += T
    print(H ,M)