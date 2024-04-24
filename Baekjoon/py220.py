import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    M, N, x, y = map(int, input().split())
    flag = True
    while x <= M * N:
        if (x - y) % N == 0:
            ans = x
            flag = False
            break
        x += M
    if flag:
        ans = -1
    print(ans)
    # a, b = 1, 1
    # cnt = 1
    # flag = True
    # while True:
    #     if a == M:
    #         a = 1
    #     else:
    #         a += 1
    #     if b == N:
    #         b = 1
    #     else:
    #         b += 1
    #     cnt += 1
    #     if a == x and b == y:
    #         break
    #     elif a == 1 and b == 1:
    #         flag = False
    #         break
    # if flag:
    #     print(cnt)
    # else:
    #     print(-1)