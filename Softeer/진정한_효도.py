batt = [list(map(int, input().split())) for _ in range(3)]

height = [1, 2, 3]
min_cnt = 10
for h in height:
    for i in range(3):
        cnt = 0
        for j in range(3):
                cnt += abs(h - batt[i][j])
        if min_cnt >= cnt:
            min_cnt = cnt
    
    for r in range(3):
        cnt = 0
        for c in range(3):
            cnt += abs(h - batt[c][r])
        if min_cnt >= cnt:
            min_cnt = cnt
print(min_cnt)