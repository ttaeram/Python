def solution(n, works):
    L = len(works)
    S = sum(works)
    if S <= n:
        answer = 0
    else:
        S -= n
        a = S // L
        m = min(works)
        cnt = 0
        arr = []
        for n in range(L):
            if works[n] < a:
                arr.append(works[n])
                cnt += 1
        L -= cnt
        S -= sum(arr)
        a = S // L
        answer = 0
        if S % L == 0:
            for l in range(L):
                answer += a ** 2
        else:
            for l in range(L):
                if l < S % L:
                    answer += (a + 1) ** 2
                else:
                    answer += a ** 2
        if arr:
            for b in arr:
                answer += b ** 2
    return answer

works = [10, 10, 1]
n = 10
ans = solution(n, works)
print(ans)