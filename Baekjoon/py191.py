import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, d = map(int, input().split())
    arr[a].append((b, d))
    arr[b].append((a, d))
for m in range(M):
    s, e = map(int, input().split())
    stack = [(s, 0)]
    check = [0] * (N + 1)
    while True:
        s, d = stack.pop()
        if s == e:
            ans = d
            break
        if not check[s]:
            check[s] = 1
            for i in arr[s]:
                stack.append((i[0], i[1] + d))
    print(ans)