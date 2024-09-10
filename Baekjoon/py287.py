import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]
mapp = []

direction = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
shark = (N//2, N//2)

def ice(d, s):
    x, y = shark[0], shark[1]
    dx = direction[d][0]
    dy = direction[d][1]

    for i in range(1, s+1):
        nx = x + dx * i
        ny = y + dy * i
        arr[nx][ny] = 0

def move():
    x, y = shark[0], shark[1]-1
    m_cnt = 1
    m_dis = 1
    balls = deque()
    balls.append(arr[x][y])
    positions = [(x, y)]
    while x > 0 or y > 0:
        if (x, y) == (0, 1):
            break
        if m_cnt:
            if m_dis % 2:
                dx, dy = 1, 0
            else:
                dx, dy = -1, 0

            for i in range(m_dis):
                x += dx
                y += dy

                if x < 0 or y < 0:
                    break

                balls.append(arr[x][y])
                positions.append((x, y))
            m_dis += 1
            m_cnt = 0
        
        else:
            if m_dis % 2:
                dx, dy = 0, -1
            else:
                dx, dy = 0, 1
            
            for i in range(m_dis):
                x += dx
                y += dy

                if x < 0 or y < 0:
                    break

                balls.append(arr[x][y])
                positions.append((x, y))
            m_cnt += 1

    cnt = 0
    for b in range(len(balls)):
        ball = balls.popleft()
        if ball != 0:
            balls.append(ball)
        else:
            cnt += 1
    for _ in range(cnt):
        balls.append(0)

    for b in range(len(balls)):
        x, y = positions[b][0], positions[b][1]
        ball = balls[b]
        arr[x][y] = ball

    return positions

def explode():
    res1, res2, res3 = 0, 0, 0
    while True:
        cand = [(shark[0], shark[1])]
        flag = True
        now = 0
        for position in mapp:
            x, y = position
            ball = arr[x][y]

            if ball == now:
                cand.append((x, y))
            else:
                if len(cand) > 3:
                    if now == 1:
                        res1 += len(cand)
                    elif now == 2:
                        res2 += len(cand)
                    else:
                        res3 += len(cand)

                    for ca in cand:
                        r, c = ca[0], ca[1]
                        arr[r][c] = 0
                    flag = False
                    cand = [(x, y)]
                    now = ball
                else:
                    cand = [(x, y)]
                    now = ball

        # if len(cand) > 3:
        #     if now == 1:
        #         res1 += len(cand)
        #     elif now == 2:
        #         res2 += len(cand)
        #     else:
        #         res3 += len(cand)

        #     for ca in cand:
        #         r, c = ca[0], ca[1]
        #         arr[r][c] = 0
        #     flag = False

        if not flag:
            move()
        else:
            break
    return (res1, res2, res3)

def end():
    cnt = 0
    now = 0
    new_balls = []
    for i in range(len(mapp)):
        x, y = mapp[i]
        ball = arr[x][y]

        if i == 0:
            cnt = 1
            now = ball
            continue
        
        if ball == 0:
            break

        if ball == now:
            cnt += 1
        else:
            new_balls.append(cnt)
            new_balls.append(now)
            cnt = 1
            now = ball
    
    for i in range(len(mapp)):
        x, y = mapp[i][0], mapp[i][1]
        if i > len(new_balls)-1:
            arr[x][y] = 0
        else:
            arr[x][y] = new_balls[i]

ans = 0
for com in commands:
    d, s = com
    ice(d, s)
    mapp = move()
    res1, res2, res3 = explode()
    ans += (res1 + 2 * res2 + 3 * res3)
    end()

print(ans)