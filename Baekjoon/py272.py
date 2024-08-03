import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = []
for _ in range(K):
    r, c, s = map(int, input().split())
    command.append((r, c, s))
