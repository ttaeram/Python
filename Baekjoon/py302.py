import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chik = []
home = []
arr = []

for i in range(N):
    semi = list(map(int, input().split()))
    for j in range(N):
        if semi[j] == 1:
            home.append((i, j))
        elif semi[j] == 2:
            chik.append((i, j))
    arr.append(semi)

check = [0] * len(chik)
ans = int(1e9)

def sol(idx, cnt):
    global ans

    if cnt == M:
        res = 0

        for h in home:
            d = int(1e9)

            for i in range(len(check)):
                if check[i]:
                    num = abs(h[0] - chik[i][0]) + abs(h[1] - chik[i][1])
                    d = min(d, num)
            
            res += d
        ans = min(res, ans)

        return
    
    for i in range(idx, len(chik)):
        if not check[i]:
            check[i] = 1
            sol(i+1, cnt+1)
            check[i] = 0

sol(0, 0)

print(ans)

# 각 집에서 치킨집까지의 거리를 싹 추합해놓고 치킨집 줄여가면서 풀면 되는거 아닐까 싶음