import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    check = [[] for _ in range(N + 2)]
    conv = [list(map(int, input().split())) for _ in range(N + 2)]
    for n in range(N + 2):
        p0 = conv[n][0]
        p1 = conv[n][1]
        for i in range(N + 2):
            h0 = conv[i][0]
            h1 = conv[i][1]
            if abs(h0 - p0) + abs(h1 - p1) <= 20 * 50:
                check[n].append(i)

    visited = [0] * (N + 2)
    stack = [0]
    flag = False
    while stack:
        pos = stack.pop()
        if not visited[pos]:
            visited[pos] = 1
            for j in check[pos]:
                stack.append(j)
                if j == N + 1:
                    ans = 'happy'
                    flag = True
                    break
    if not flag:
        ans = 'sad'
    print(ans)
            
    #     x, y = map(int, input().split())
    #     if n == 0:
    #         home = (x, y)
    #     elif n == (N + 1):
    #         rock = (x, y)
    #     else:
    #         conv.append((x, y))
    # if abs(rock[0] - home[0]) + abs(rock[1] - home[1]) <= 20 * 50:
    #     ans = 'happy'
    #     print(ans)
    #     continue
    # conv.sort()

    # if (abs(rock[0]) + abs(rock[1])) - (abs(home[0]) + abs(home[1])) <= 20 * 50:
    #     ans = 'happy'
    #     print(ans)
    #     continue
    # conv.sort()
    # for n in range(N):
    #     if (abs(conv[n][0]) + abs(conv[n][1])) - (abs(home[0]) + abs(home[1])) <= 20 * 50:
    #         home = conv[n]
    #     else:
    #         ans = 'sad'
    #     if (abs(rock[0]) + abs(rock[1])) - (abs(home[0]) + abs(home[1])) <= 20 * 50:
    #         ans = 'happy'
    # print(ans)