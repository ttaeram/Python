import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for i in range(1, N + 1):
    n = input().strip()
    dic[i] = n
    dic[n] = i

for m in range(M):
    q = input().strip()
    if q.isalpha():
        print(dic[q])
    else:
        print(dic[int(q)])
# arr = [input().strip() for _ in range(N)]
# Q = [input().strip() for __ in range(M)]
# res = []

# for q in range(M):
#     if Q[q].isalpha():
#         print(arr.index(Q[q]) + 1)
#     if Q[q].isnumeric():
#         print(arr[int(Q[q]) - 1])
