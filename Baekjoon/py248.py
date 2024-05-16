import sys
input = sys.stdin.readline

direction = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
n_arr = [['S'] * M for _ in range(N)]

for r in range(R):
    Xo, Yo, D = map(str, input().split())
    dx = direction[D][0]
    dy = direction[D][1]
    Xo, Yo = int(Xo) - 1, int(Yo) - 1
    stack = [(Xo, Yo)]
    while stack:
        x, y = stack.pop()
        if n_arr[x][y] == 'S':
            n_arr[x][y] = 'F'
            nx, ny = x, y
            for i in range(arr[Xo][Yo]):
                nx += dx
                ny += dy
                if 0 <= nx < N and 0 <= ny < M and n_arr[nx][ny] == 'S':
                    stack.append((nx, ny))
    Xd, Yd = map(int, input().split())
    n_arr[Xd - 1][Yd - 1] = 'S'

    print(n_arr)