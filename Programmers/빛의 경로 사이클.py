def solution(grid):
    answer = []
    l_2 = len(grid[0])
    l_1 = len(grid)
    start = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    res_lst = []
    for r in range(l_1):
        for c in range(l_2):
            for dir_1 in start:
                x_1 = dir_1[0]
                y_1 = dir_1[1]
                pos_1 = [r, c]
                # if (dir_1, pos_1) in res_lst:
                #     continue
                if grid[pos_1[0]][pos_1[1]] == 'S':
                    direction = [x_1, y_1]
                elif grid[pos_1[0]][pos_1[1]] == 'R':
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
                # res = (dir_1, pos_1)
                # res_lst.append(res)
                res = (direction, pos)
                res_lst.append(res)
                cnt = 1
                while True:
                    if pos == pos_1 and direction == dir_1:
                        answer.append(cnt)
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
                    res = (direction, pos)
                    if res in res_lst:
                        break
                    res_lst.append(res)
                    cnt += 1
    answer.sort()
    return answer

grid = ['S', 'S']
print(solution(grid))
