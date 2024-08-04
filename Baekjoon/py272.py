from collections import deque
from itertools import permutations
from copy import deepcopy
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = deque()
for _ in range(K):
    r, c, s = map(int, input().split())
    command.append((r, c, s))
operation = permutations(command)
ans = int(1e9)

def find_min(ans):
    for n in range(N):
        ans = min(ans, sum(arr_2[n]))
    return ans

def find_d(x, y, x_d, y_d):
    if y_d == 1 and y == c + i:
        x_d = 1
        y_d = 0
    elif x_d == 1 and x == r + i:
        x_d = 0
        y_d = -1
    elif y_d == -1 and y == c - i:
        x_d = -1
        y_d = 0
    return (x_d, y_d)


def rotate(r, c, i):
    pos = []
    semi = deque()
    x, y = r - i, c - i
    check = set()
    x_d, y_d = 0, 1
    while (x, y) not in check:
        pos.append((x, y))
        semi.append(arr_2[x][y])
        check.add((x, y))
        x_d, y_d = find_d(x, y, x_d, y_d)
        x += x_d
        y += y_d
    change = semi.pop()
    semi.appendleft(change)
    for i in range(len(semi)):
        x, y = pos[i]
        arr_2[x][y] = semi[i]

for command in operation:
    arr_2 = deepcopy(arr)
    for rcs in command:
        r, c, s = rcs
        r -= 1
        c -= 1
        for i in range(1, s+1):
            rotate(r, c, i)
    ans = find_min(ans)

print(ans)