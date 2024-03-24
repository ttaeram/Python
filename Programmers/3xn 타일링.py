def solution(n):
    rn = n // 2
    arr = [0] * 2501
    arr[1] = 3
    arr[2] = 11
    if rn > 2:
        for i in range(3, rn + 1):
            arr[i] = arr[i - 2] * 3 + arr[i - 1] * 4
    answer = arr[rn]
    return answer

n = 4
print(solution(n))