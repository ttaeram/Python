import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x_list = []
y_list = []

for i in range(w):
    x_list.append(i)
for j in range(w, 0, -1):
    x_list.append(j)

for k in range(h):
    y_list.append(k)
for l in range(h, 0, -1):
    y_list.append(l)

x = x_list[(p + t) % (2 * w)]
y = y_list[(q + t) % (2 * h)]

print(x, y)
# x = p
# y = q
# time = 0
# x_pm = 1
# y_pm = 1

# while True:
#     if x == w:
#         x_pm = -1
#     elif x == 0:
#         x_pm = 1
    
#     if y == h:
#         y_pm = -1
#     elif y == 0:
#         y_pm = 1
    
#     if x_pm == 1:
#         x += 1
#     elif x_pm == -1:
#         x -= 1

#     if y_pm == 1:
#         y += 1
#     elif y_pm == -1:
#         y -= 1
    
#     time += 1
    
#     if time == t:
#         print(x, y)
#         break