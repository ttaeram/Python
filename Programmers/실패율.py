def solution(N, stages):
    dic = {0: 0}
    arr = [0] * (N + 1)
    L = len(stages)
    for n in range(1, N + 2):
        dic[n] = stages.count(n)
    
    for i in range(1, N + 1):
        if dic[i] == 0:
            arr[i] = (i, 0)
            L = L - dic[i - 1]
        else:
            L = L - dic[i - 1]
            arr[i] = (i, dic[i] / L)
    
    arr.pop(0)
    arr.sort(key = lambda x: (-x[1], x[0]))
    answer = []
    for j in range(len(arr)):
        answer.append(arr[j][0])
    return answer

N = 5
stages = [2, 1, 3, 5, 6, 6, 6]

ans = solution(N, stages)
print(ans)