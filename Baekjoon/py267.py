import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
check = [0] * 9
pos = [0] * 9
pos[3] = 0
check[3] = 1
ans = 0

def game(res):
    global ans
    if res == 9:
        idx = 0
        score = 0
        for g in arr:
            out = 0
            lu1, lu2, lu3 = 0, 0, 0
            while out <= 2:
                taja = pos[idx]
                if g[taja] == 0:
                    out += 1
                elif g[taja] == 1:
                    score += lu3
                    lu1, lu2, lu3 = 1, lu1, lu2
                elif g[taja] == 2:
                    score += lu2 + lu3
                    lu1, lu2, lu3 = 0, 1, lu1
                elif g[taja] == 3:
                    score += lu1 + lu2 + lu3
                    lu1, lu2, lu3 = 0, 0, 1
                else:
                    score += lu1 + lu2 + lu3 + 1
                    lu1, lu2, lu3 = 0, 0, 0
                idx += 1
                idx %= 9
        ans = max(ans, score)
        return
    
    for i in range(9):
        if check[i]:
            continue
        else:
            check[i] = 1
            pos[i] = res
            game(res + 1)
            check[i] = 0
            pos[i] = 0
game(1)
print(ans)