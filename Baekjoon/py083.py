N,M =map(int,input().split())
board = []

for _ in range(N): # 체스판양식 저장
    board.append(list(input()))
c = 0
for i in range(N-7): # 체스판 첫번째 칸 돌기
    for j in range(M-7):
        black = 0
        for a in range(8): # 체스판 8*8호출
            for b in range(8):
                if (a+b) %2 ==0: #임의로 첫칸을 검은색으로 지정시 맞게 칠한 개수 구하기
                    black += (board[a+i][b+j]=="B")
                else:
                    black += (board[a+i][b+j]=="W")    
        if black < 32: #첫칸이 검은색일 경우 틀린 칸이 과반수보다 많은 경우 첫칸을 흰색으로 결정
            black = 64 - black
        if c < black:
            c=black # 맞은 칸의 최대값 비교
print(64-c)

# N, M = map(int, input().split())

# board = []
# for i in range(N):
#     board.append(input())

# print(board)
# result = []

# for i in range(N-7):
#     for j in range(M-7):
#         black = 0
#         white = 0

#         for a in range(i, i + 8):
#             for b in range(j, j + 8):
#                 if (a + b) % 2 == 0:
#                     if board[a][b] != 'B':
#                         black += 1
#                     if board[a][b] != 'W':
#                         white += 1
#                 else:
#                     if board[a][b] != 'W':
#                         black += 1
#                     if board[a][b] != 'B':
#                         white += 1
        
#         result.append(black)
#         result.append(white)

# print(min(result))

# def BruteForce(p, t):
#     i = 0
#     j = 0
#     while i < len(t) and j < len(p):
#         if t[i] != p[j]:
#             i = i - j
#             j = -1
#         i += 1
#         j += 1
#     if j == len(p):
#         return i - len(p)
#     else:
#         return -1

# pattern = 'Python'
# text = 'Hello Python World'
# print(BruteForce(pattern, text))