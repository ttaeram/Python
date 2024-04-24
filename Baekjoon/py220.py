import sys
input = sys.stdin.readline

def sol():
    le = []
    sn = []
    N, M = map(int, input().split())
    for _ in range(N):
        a, b = map(int, input().split())
        le.append((a, b))
    for _ in range(M):
        a, b = map(int, input().split())
        sn.append((a, b))
    arr = [0] * 101
    for i in range(101):
        