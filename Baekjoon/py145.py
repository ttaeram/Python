N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

land_info = {}
time = 100000000
level = 0

for n in range(N):
    for m in range(M):
        if land[n][m] in land_info:
            land_info[land[n][m]] += 1
        elif land[n][m] not in land_info:
            land_info[land[n][m]] = 1

land_keys = sorted(list(land_info.keys()))

for tar in range(257):
    use_block = 0
    dig_block = 0
    for i in land_keys:
        if i < tar:
            use_block += (tar - i) * land_info[i]
        else:
            dig_block += (i - tar) * land_info[i]
    
    if dig_block + B < use_block:
        continue

    res = 2 * dig_block + use_block
    if res <= time:
        time = res
        level = tar

print(time, level)