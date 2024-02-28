def solution(board, moves):
    N = len(board)
    stack = []
    cnt = 0
    flag = True
    for turn in moves:
        index = turn - 1
        for i in range(N):
            flag = True
            for j in range(N):
                if j == index:
                    if board[i][j] != 0:
                        stack.append(board[i][j])
                        if len(stack) > 1:
                            if stack[-1] == stack[-2]:
                                stack.pop()
                                stack.pop()
                                cnt += 2
                        board[i][j] = 0
                        flag = False
                        break
            if flag == False:
                break
    answer = cnt
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
ans = solution(board, moves)
print(ans)