import sys
input = sys.stdin.readline

N, K = map(int, input().split())
color = [[] for _ in range(K + 1)]
for n in range(N):
    x, y, k = map(int, input().split())
    color[k].append((x, y))

min_s = 2001 ** 2
if K == 1:
    min_s = 0

elif K >= 2:
    for i in range(1, K + 1):
        for j in range(len(color[i])):
            x1, y1 = color[i][j]
            for l in range(i, K + 1):
                for m in range(len(color[l])):
                    x2, y2 = color[l][m]
                    cnt = 0
                    for o in range(1, K + 1):
                        for p in color[o]:
                            if x1 <= p[0] <= x2:
                                if y1 <= p[1] <= y2 or y2 <= p[1] <= y1:
                                    cnt += 1
                                    break
                            elif x2 <= p[0] <= x1:
                                if y1 <= p[1] <= y2 or y2 <= p[1] <= y1:
                                    cnt += 1
                                    break

                        if cnt == K:
                            if min_s > abs(x1 - x2) * abs(y1 - y2):
                                min_s = abs(x1 - x2) * abs(y1 - y2)

print(min_s)