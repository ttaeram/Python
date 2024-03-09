import sys
input = sys.stdin.readline

# T = int(input())
# for t in range(T):
#     M, N, K = map(int, input().split())
#     arr = []
#     stack = []
#     cnt = 0
#     for k in range(K):
#         x, y = map(int, input().split())
#         if not stack:
#             stack.append((x, y))
#             cnt += 1
#         else:
#             if (x - 1, y) in stack or (x, y - 1) in stack:
#                 stack.append((x, y))
#             else:
#                 stack = []
#     print(cnt)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def bug(x, y):
    global flag
    if x < 0 or x >= M or y < 0 or y >= N:
        flag = False
        return flag
    if arr[y][x] == 1:
        arr[y][x] = 0
        bug(x + 1, y)
        bug(x, y + 1)
        bug(x - 1, y)
        bug(x, y - 1)
        return flag
    flag = False
    return flag

T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    
    flag = True
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if bug(i, j) == True:
                cnt += 1
            # if arr[i][j] == 1:
            #     while True:
            #         oi = i
            #         oj = j
            #         for k in range(4):
            #             ni = i + di[k]
            #             nj = j + dj[k]
            #             if 0 <= ni < N and 0 <= nj < M:
            #                 if arr[ni][nj] == 1:
            #                     arr[i][j] = 0
            #                     i = ni
            #                     j = nj
            #         if oi == i and oj == j:
            #             arr[i][j] = 0
            #             break
            #     cnt += 1
    
    print(cnt)