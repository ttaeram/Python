from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
odd = ('R', 'G')

N = int(input())
arr = [list(map(str, input().strip())) for _ in range(N)]
check_1 = set()
check_2 = set()
cnt_1 = 0
cnt_2 = 0
for r in range(N):
    for c in range(N):
        if (r, c) not in check_1:
            stack_1 = deque([(r, c)])
            while stack_1:
                x, y = stack_1.popleft()
                color = arr[x][y]
                if (x, y) not in check_1:
                    check_1.add((x, y))
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == color:
                                stack_1.append((nx, ny))
            cnt_1 += 1
        elif (r, c) not in check_2:
            stack_2 = deque([(r, c)])
            while stack_2:
                a, b = stack_2.popleft()
                color_ = arr[a][b]
                if (a, b) not in check_2:
                    check_2.add((a, b))
                    for j in range(4):
                        na = a + dx[j]
                        nb = b + dy[j]
                        if 0 <= na < N and 0 <= nb < N:
                            if (color in odd and arr[nx][ny] in odd) or arr[nx][ny] == color:
                                stack_2.append((na, nb))
            cnt_2 += 1
print(cnt_1, cnt_2)
