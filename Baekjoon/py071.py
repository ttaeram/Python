N = int(input())
white_board = [[0] * 100 for _ in range(100)]
 
for _ in range(N):
    a, b = map(int, input().split())
 
    for i in range(b, b + 10):
        for j in range(a, a + 10):
            white_board[i][j] = 1
 
cnt = 0
for i in range(100):
    for j in range(100):
        if white_board[i][j]:
            cnt += 1
 
print(cnt)

# N = int(input())

# paper = []
# for i in range(N):
#     paper.append(list(map(int, input().split())))

# x = []
# y = []
# for pa in paper:
#     x.append(pa[0])
#     y.append(pa[1])

# x_sort = sorted(x)
# y_sort = sorted(y)

# if x_sort[2] - x_sort[0] < 10 and y_sort[2] - y_sort[0] < 10 and x_sort[2] - x_sort[1] < 10 and y_sort[2] - y_sort[1] < 10 and x_sort[1] - x_sort[0] < 10 and y_sort[1] - y_sort[0] < 10:
#     result = (10 - (x_sort[2] - x_sort[0])) * (10 - (y_sort[2] - y_sort[0])) + (10 - (x_sort[1] - x_sort[0])) * (10 - (y_sort[1] - y_sort[0])) + (10 - (x_sort[2] - x_sort[1])) * (10 - (y_sort[2] - y_sort[1])) - 2 * ((10 - (x_sort[2] - x_sort[0])) * (10 - (y_sort[2] - y_sort[1])))
# elif x_sort[2] - x_sort[1] < 10 and y_sort[2] - y_sort[1] < 10 and x_sort[1] - x_sort[0] < 10 and y_sort[1] - y_sort[0] < 10:
#     result = (10 - (x_sort[2] - x_sort[1])) * (10 - (y_sort[2] - y_sort[1])) + (10 - (x_sort[1] - x_sort[0])) * (10 - (y_sort[1] - y_sort[0]))
# elif x_sort[1] - x_sort[0] < 10 and y_sort[1] - y_sort[0] < 10:
#     result = (10 - (x_sort[1] - x_sort[0])) * (10 - (y_sort[1] - y_sort[0]))
# elif x_sort[2] - x_sort[1] < 10 and y_sort[2] - y_sort[1] < 10:
#     result = (10 - (x_sort[2] - x_sort[1])) * (10 - (y_sort[2] - y_sort[1]))

# print(300 - result)