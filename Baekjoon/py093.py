K, N =  map(int, input().split())

LAN = []
for _ in range(K):
    LAN.append(int(input()))
LAN = sorted(LAN)

min_lan = LAN[0] // 2
cnt = 0
for n in LAN:
    cnt += n // min_lan

print(cnt)