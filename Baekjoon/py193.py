import sys
input = sys.stdin.readline

def paper(x, y, n):
    global res_0, res_1
    color = arr[x][y]
    for r in range(x, x + n):
        for c in range(y, y + n):
            if color != arr[r][c]:
                paper(x, y, n//2)
                paper(x + n//2, y, n//2)
                paper(x, y + n//2, n//2)
                paper(x + n//2, y + n//2, n//2)
                return
    if not color:
        res_0 += 1
    else:
        res_1 += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res_0 = 0
res_1 = 0
paper(0, 0, N)
print(res_0)
print(res_1)