import sys
import copy
from collections import deque
input = sys.stdin.readline
H, W = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(H)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

cnt = 1
for k in range(H):
    for g in range(W):
        if arr[k][g] == '#':
            cnt += 1
print(cnt)
for h in range(H):
    for w in range(W):
        if arr[h][w] == '#':
            arr_r = copy.deepcopy(arr)
            stack = deque()
            BFS = []
            visited = [[0] * 25 for __ in range(25)]
            a, b = h, w
            stack.append((a, b))
            BFS.append((a, b))
            bp = True
            while stack:
                a, b = stack.popleft()
                for i in range(4):
                    ni = a + di[i]
                    nj = b + dj[i]
                    nii = a + di[i] * 2
                    njj = b + dj[i] * 2
                    if 0 <= nii < H and 0 <= njj < W:
                        if arr_r[nii][njj] == '#':
                            if arr_r[ni][nj] == '#':
                                if visited[nii][njj] == 0:
                                    visited[nii][njj] = 1
                                    BFS.append((nii, njj))
                                    stack.append((nii, njj))
                                    arr_r[a][b] = '.'
                                    arr_r[ni][nj] = '.'
                                    if len(BFS) == 2:
                                        if BFS[0][0] + 2 == BFS[1][0]:
                                            fd = 'V'
                                            x, y = (2, 0)
                                        elif BFS[0][1] + 2 == BFS[1][1]:
                                            fd = '>'
                                            x, y = (0, 2)
                                        elif BFS[0][0] - 2 == BFS[1][0]:
                                            fd = '^'
                                            x, y = (-2, 0)
                                        elif BFS[0][1] - 2 == BFS[1][1]:
                                            fd = '<'
                                            x, y = (0, -2)
                                            
                                        nx, ny = nii - BFS[-1][0], njj - BFS[-1][1]
                                        if (nx, ny) == (x, y):
                                            print('A', end = '')
                                            x, y = nx, ny

                                        elif (x, y) == (0, 2) or (x, y) == (0, -2):
                                            if (nx, ny) == (y, x):
                                                print('RA', end = '')
                                            else:
                                                print('LA', end = '')
                                        else:
                                            if (nx, ny) == (y, x):
                                                print('LA', end = '')
                                            else:
                                                print('RA', end = '')
                if len(BFS) >= 2:
                    for bf in range(len(BFS) - 1):
                        if abs(BFS[bf][0] - BFS[bf + 1][0]) > 2 or abs(BFS[bf][1] - BFS[bf + 1][1]) > 2:
                            bp = False
                if not bp:
                    break
            if len(BFS) * 2 == cnt:
                print(BFS[0][0] + 1, BFS[0][1] + 1)
                print(fd)
                print(BFS)
                exit(0)