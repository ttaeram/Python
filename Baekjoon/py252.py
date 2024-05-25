from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
arr = []
shark = tuple()
for r in range(N):
    a = list(map(int, input().split()))
    if not shark:
        for c in range(N):
            if a[c] == 9:
                shark = (r, c)
                break
    arr.append(a)
ans = 0
def bfs(x, y):
    visited = [[0] * N for _ in range(N)]
    queue = deque([[x,y]])
    cand = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for idx in range(4):
            ii, jj = i + dx[idx] , j + dy[idx]

            if 0 <= ii and ii < N and 0 <= jj and jj < N and visited[ii][jj] == 0:
                if arr[x][y] > arr[ii][jj] and arr[ii][jj] != 0:
                    visited[ii][jj] =  visited[i][j] + 1
                    cand.append((visited[ii][jj] - 1, ii, jj))
                elif arr[x][y] == arr[ii][jj]:
                    visited[ii][jj] =  visited[i][j] + 1
                    queue.append([ii,jj])
                elif arr[ii][jj] == 0:
                    visited[ii][jj] =  visited[i][j] + 1
                    queue.append([ii,jj])
    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))


i, j = shark
size = [2, 0]
while True:
    arr[i][j] = size[0]
    cand = deque(bfs(i,j))
    if not cand:
        break 
    step, xx, yy = cand.popleft()
    ans += step
    size[1] += 1
    
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    arr[i][j] = 0
    i, j = xx, yy
        
print(ans)