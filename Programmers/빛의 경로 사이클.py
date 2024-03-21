def solution(grid):
    answer = []
    l_2 = len(grid[0])
    l_1 = len(grid)
    start = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res_lst = set()
    for r in range(l_1):
        for c in range(l_2):
            for dir_1 in start:
                pos_1 = (r, c)
                pos = (r, c)
                direction = dir_1
                if (dir_1, pos_1) in res_lst:
                    continue
                res = (dir_1, pos_1)
                res_lst.add(res)
                cnt = 0
                while True:
                    res = ()
                    if res in res_lst:
                        break
                    x = direction[0]
                    y = direction[1]
                    if grid[pos[0]][pos[1]] == 'S':
                        direction = (x, y)
                    elif grid[pos[0]][pos[1]] == 'R':
                        if direction == (0, 1) or direction == (0, -1):
                            direction = (y, x)
                        else:
                            direction = (y, -x)
                    else:
                        if direction == (0, 1) or direction == (0, -1):
                            direction = (-y, x)
                        else:
                            direction = (y, x)
                    
                    pos = (pos[0] + direction[0], pos[1] + direction[1])
                    if pos[0] == -1:
                        pos = (l_1 - 1, pos[1])
                    elif pos[0] == l_1:
                        pos = (0, pos[1])
                    if pos[1] == -1:
                        pos = (pos[0], l_2 - 1)
                    elif pos[1] == l_2:
                        pos = (pos[0], 0)
                    res = (direction, pos)
                    res_lst.add(res)
                    cnt += 1
                    if pos == pos_1 and direction == dir_1:
                        answer.append(cnt)
                        break
    answer.sort()
    return answer

grid = ['S', 'S']
print(solution(grid))
