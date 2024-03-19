from collections import deque
def solution(grid):
    answer = []
    l_2 = len(grid[0])
    l_1 = len(grid)
    start = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    res_lst = []
    for dir_1 in start:
        start_dic = {(0, 1): 1, (0, -1): 2, (1, 0): 3, (-1, 0): 4}
        res = deque()
        x_1 = dir_1[0]
        y_1 = dir_1[1]
        pos_1 = [0, 0]
        if grid[0][0] == 'S':
            direction = [x_1, y_1]
        elif grid[0][0] == 'R':
            if dir_1 == [0, 1] or dir_1 == [0, -1]:
                direction = [y_1, x_1]
            else:
                direction = [y_1, -x_1]
        else:
            if dir_1 == [0, 1] or dir_1 == [0, -1]:
                direction = [-y_1, x_1]
            else:
                direction = [y_1, x_1]
        pos = [direction[0], direction[1]]
        if pos[0] == -1:
            pos[0] = l_1 - 1
        elif pos[0] == l_1:
            pos[0] = 0
        if pos[1] == -1:
            pos[1] = l_2 - 1
        elif pos[1] == l_2:
            pos[1] = 0

        res.append(start_dic[tuple(direction)])
        cnt = 1
        flag = True
        while flag:
            if pos == pos_1 and direction == dir_1:
                if not res_lst:
                    res_lst.append(res)
                    answer.append(cnt)
                    break
                else:
                    for i in range(len(res)):
                        res.append(res.popleft())
                        if res in res_lst:
                            flag = False
                    if flag:
                        res_lst.append(res)
                        answer.append(cnt)
                        break
                    else:
                        break

            else:
                x = direction[0]
                y = direction[1]
                if grid[pos[0]][pos[1]] == 'S':
                    direction = [x, y]
                elif grid[pos[0]][pos[1]] == 'R':
                    if direction == [0, 1] or direction == [0, -1]:
                        direction = [y, x]
                    else:
                        direction = [y, -x]
                else:
                    if direction == [0, 1] or direction == [0, -1]:
                        direction = [-y, x]
                    else:
                        direction = [y, x]
                
                pos = [pos[0] + direction[0], pos[1] + direction[1]]
                if pos[0] == -1:
                    pos[0] = l_1 - 1
                elif pos[0] == l_1:
                    pos[0] = 0
                if pos[1] == -1:
                    pos[1] = l_2 - 1
                elif pos[1] == l_2:
                    pos[1] = 0
            res.append(start_dic[tuple(direction)])
            cnt += 1

    return answer

grid = ["S"]
print(solution(grid))
