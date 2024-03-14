import sys
import copy
from collections import deque
input = sys.stdin.readline
H, W = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(H)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

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
            while stack:
                a, b = stack.pop()
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
            print(BFS)