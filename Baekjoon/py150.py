import sys
input = sys.stdin.readline

dic = {}
N, M = map(int, input().split())
for n in range(N):
    a, b = map(str, input().split())
    dic[a] = b

for m in range(M):
    print(dic[input().strip()])
