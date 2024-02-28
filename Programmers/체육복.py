def solution(n, lost, reserve):
    for j in range(len(lost)):
        if lost[j] in reserve:
            reserve[reserve.index(lost[j])] = -2
            lost[j] = -2
    lost.sort()
    reserve.sort()

    for i in range(len(lost)):
        if lost[i] - 1 in reserve:
            reserve[reserve.index(lost[i] - 1)] = -2
            lost[i] = -2
            continue
        elif lost[i] + 1 in reserve:
            reserve[reserve.index(lost[i] + 1)] = -2
            lost[i] = -2
            continue
    answer = n - (len(lost) - lost.count(-2))
    return answer

n = 4
lost = [2, 3]
reserve = [3, 4]

ans = solution(n, lost, reserve)
print(ans)