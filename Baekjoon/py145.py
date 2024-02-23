N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

land_info = {}
time = 0

for n in range(N):
    for m in range(M):
        if land[n][m] in land_info:
            land_info[land[n][m]] += 1
        elif land[n][m] not in land_info:
            land_info[land[n][m]] = 1

for k, v in land_info.items():
    if v == max(land_info.values()):
        tar = k

land_keys = land_info.keys().sort()
for i in range(len(land_keys)):
    if land_keys[i] == tar:
        continue
    elif land_keys[i] < tar:
        while land_info[land_keys[i]] != 0:
            if B != 0:
                B -= 1
                land_info[land_keys[i]] -= 1
                time += 1
            else:

print(land_info)