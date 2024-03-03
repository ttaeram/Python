X, Y = map(int, input().split())
N = int(input())

lst_0 = []
lst_1 = []
for n in range(N):
    a, b = map(int, input().split())
    if a == 0:
        lst_0.append(b)
    else:
        lst_1.append(b)

lst_0.append(Y)
lst_1.append(X)

lst_0.sort()
lst_1.sort()

max_x = lst_1[0]
max_y = lst_0[0]
for y in range(1, len(lst_0)):
    leng = lst_0[y] - lst_0[y - 1]
    if max_y < leng:
        max_y = leng
for x in range(1, len(lst_1)):
    leng_ = lst_1[x] - lst_1[x - 1]
    if max_x < leng_:
        max_x = leng_

print(max_x * max_y)