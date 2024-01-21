mal = list(map(int, input().split()))

right_mal = [1, 1, 2, 2, 2, 8]

need_mal = []
for a in range(len(right_mal)):
    need_mal.append(right_mal[a] - mal[a])

for i in need_mal:
    print(i, end = ' ')