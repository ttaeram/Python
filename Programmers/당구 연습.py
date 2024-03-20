def solution(m, n, startX, startY, balls):
    answer = []
    pos = [startX, startY]
    for i in range(len(balls)):
        des = [balls[i][0], balls[i][1]]
        ans = 10**10
        res = []
        if pos[0] != des[0] or pos[1] > des[1]: 
            res.append(abs(pos[0] - des[0]) ** 2 + abs(2 * n - pos[1] - des[1]) ** 2)
        if pos[0] != des[0] or pos[1] < des[1]: 
            res.append(abs(pos[0] - des[0]) ** 2 + abs(pos[1] + des[1]) ** 2)
        if pos[1] != des[1] or pos[0] < des[0]: 
            res.append(abs(pos[0] + des[0]) ** 2 + abs(pos[1] - des[1]) ** 2)
        if pos[1] != des[1] or pos[0] > des[0]: 
            res.append(abs(2 * m - pos[0] - des[0]) ** 2 + abs(pos[1] - des[1]) ** 2)
        for r in res:
            if ans > r:
                ans = r
        answer.append(ans)
    return answer