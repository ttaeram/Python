from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

direction = {
    1: [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]],
    2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
    3: [[(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)]],
    4: [[(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)], [(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)]],
    5: [[(0, 1), (1, 0), (-1, 0), (0, -1)]]
}

def findCctvs():
    for n in range(N):
        for m in range(M):
            if arr[n][m] != 6 and arr[n][m] != 0:
                cctvs.append((n, m, arr[n][m]))

cctvs = deque()

findCctvs()

def watch(x, y, dx, dy, arr):
    distance = 1
    while True:
        nx, ny = x + dx * distance, y + dy * distance
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 6:
                break
            elif arr[nx][ny] in [1, 2, 3, 4, 5]:
                break
            else:
                arr[nx][ny] = '#'
        
        else:
            break
        distance += 1

def copy(arr):
    semi = []
    for i in range(N):
        ssemi = []
        for j in arr[i]:
            ssemi.append(j)
        semi.append(ssemi)
    return semi

def sol(arr, idx):
    global ans

    semi = copy(arr)

    if idx == len(cctvs):
        cnt = 0
        for i in semi:
            cnt += i.count(0)
        ans = min(ans, cnt)
        return

    x, y, direct = cctvs[idx]

    for d in direction[direct]:
        semi = copy(arr)
        for dx, dy in d:
            watch(x, y, dx, dy, semi)
        sol(semi, idx+1)

ans = 1e9
sol(arr, 0)
print(ans)