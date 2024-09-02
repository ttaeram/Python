import sys
input = sys.stdin.readline

T, W = map(int, input().split())
arr = list(int(input()) for _ in range(T))

count = {1: [], 2: []}
cnt_list = []

cnt = 0
now = 1
for i in range(T):
    if arr[i] == now:
        cnt += 1
        
    else:
        count[now].append(cnt)
        cnt = 1
        now = arr[i]

count[now].append(cnt)

for i in range(1, 3):
    count[i].sort()

ans = T
if count[1][0] == 0:
    moves = len(count[1]) + len(count[2]) - 1
    count[1].pop(0)
else:
    moves = len(count[1]) + len(count[2]) - 1

dif = moves-W

if moves % 2 == 1:
    if dif % 2 == 0:
        for n in range(dif):
            if count[1][0] > count[2][0]:
                ans -= count[2].pop(0)
            else:
                ans -= count[1].pop(0)
    else:
        for n in range(dif//2 + 1):
            if count[1][0] > count[2][0]:
                ans -= count[2].pop(0)
            else:
                ans -= count[1].pop(0)

else:
    if dif % 2 == 0:
        for n in range(dif//2):
            if count[1][0] > count[2][0]:
                ans -= count[2].pop(0)
            else:
                ans -= count[1].pop(0)
    else:
        for n in range(dif//2 + 1):
            if count[1][0] > count[2][0]:
                ans -= count[2].pop(0)
            else:
                ans -= count[1].pop(0)

print(ans)
print(count)
