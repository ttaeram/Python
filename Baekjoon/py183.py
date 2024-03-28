import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
flag = True
for n in range(N):
    arrr = list(map(str, input().strip()))
    arr.append(arrr)
    if flag:
        for a in range(M):
            if arr[n][a] == 'I':
                start = (n, a)
                flag = False
                break

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
stack = [start]
visited = [[0] * M for _ in range(N)]
visited[start[0]][start[1]] = 1
cnt = 0
while stack:
    x, y = stack.pop()
    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] != 'X' and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                stack.append((nr, nc))

                if arr[nr][nc] == 'P':
                    cnt += 1

if cnt == 0:
    ans = 'TT'        
else:
    ans = cnt            
print(ans)