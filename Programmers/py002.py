def solution(n):
    answer = 0
    arr = [0, 0] + [1] * (n - 1)
    primes = []
    cnt = 0

    for i in range(2, n + 1):
        if arr[i]:
            primes.append(i)
            for j in range(i, n + 1, i):
                if arr[j] == 1:
                    arr[j] = 0
            
    answer = len(primes)
    return answer

n = int(input())
print(solution(n))