from collections import deque
def solution(n, computers):
    answer = 0
    check = [0] * n
    for i in range(n):
        if not check[i]:
            check[i] = 1
            stack = deque([i])
            while stack:
                pos = stack.popleft()
                for j in range(n):
                    if computers[pos][j] == 1 and not check[j]:
                        check[j] = 1
                        stack.append(j)
            answer += 1
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))