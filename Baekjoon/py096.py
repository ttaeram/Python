arr_x = []
arr_y = []

for i in range(3):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

for a in range(3):
    if arr_x.count(arr_x[a]) == 1 or arr_x.count(arr_x[a]) == 3:
        new_x = arr_x[a]
    if arr_y.count(arr_y[a]) == 1 or arr_y.count(arr_y[a]) == 3:
        new_y = arr_y[a]

print(new_x, new_y)