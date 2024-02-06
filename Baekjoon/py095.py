x, y, w, h = map(int, input().split())

distance = []
distance.append(w - x)
distance.append(h - y)
distance.append(x)
distance.append(y)

print(min(distance))