N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(input())

print(board)
result = []

for i in range(N-7):
    for j in range(M-7):
        black = 0
        white = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        black += 1
                    if board[a][b] != 'W':
                        white += 1
                else:
                    if board[a][b] != 'W':
                        black += 1
                    if board[a][b] != 'B':
                        white += 1
        
        result.append(black)
        result.append(white)

print(min(result))
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