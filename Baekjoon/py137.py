N = int(input())

man = []
arr = [0] * N
for n in range(N):
    a, b = map(int, input().split())
    man.append([a, b])

man.sort()
for i in range(N - 1):
    if man[i][1] > man[i + 1][1]:
        arr[i] = 