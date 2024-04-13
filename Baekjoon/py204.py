import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    conv = []
    beer = 20
    for n in range(N + 2):
        x, y = map(int, input().split())
        if n == 0:
            home = (x, y)
        elif n == (N + 1):
            rock = (x, y)
        else:
            conv.append((x, y))
    if (abs(rock[0]) + abs(rock[1])) - (abs(home[0]) + abs(home[1])) <= 20 * 50:
        ans = 'happy'
        print(ans)
        continue
    conv.sort()
    for n in range(N):
        if (abs(conv[n][0]) + abs(conv[n][1])) - (abs(home[0]) + abs(home[1])) <= 20 * 50:
            home = conv[n]
        else:
            ans = 'sad'
        if (abs(rock[0]) + abs(rock[1])) - (abs(home[0]) + abs(home[1])) <= 20 * 50:
            ans = 'happy'
    print(ans)
