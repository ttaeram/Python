def DFS(level):
    if level == M:
        path = total
        aaa.append(path)
        return
    for i in range(4):
        total[level] = elements[i]
        DFS(level + 1)
        total[level] = ''

N, M = map(int, input().split())
arr = [list(map(str, input().split())) for _ in range(N)]
elements = ['a', 'c', 'g', 't']
total = [''] * M
aaa = []

DFS(0)
print(aaa)