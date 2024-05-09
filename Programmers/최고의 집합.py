def solution(n, s):
    if s < n:
        ans = [-1]
        return ans
    res = s // n
    etc = s % n
    ans = [res] * n
    if etc:
        for i in range(etc):
            ans[i] += 1
        ans.sort()
        return ans
    else:
        ans.sort()
        return ans

print(solution(2, 9))