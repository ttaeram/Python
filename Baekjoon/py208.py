import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = []

check = set()
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1 and (r, c) not in check:
            stack = [(r, c)]
            cnt = 0
            while stack:
                x, y = stack.pop()
                if (x, y) not in check:
                    check.add((x, y))
                    cnt += 1
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 1:
                                stack.append((nx, ny))
            answer.append(cnt)
answer.sort()
ans = len(answer)
print(ans)
print(*answer, sep='\n')