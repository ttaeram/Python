def solution(s):
    answer = s[0].upper()

    for i in range(1, len(s)):
        if s[i - 1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer
    # arr = list(map(str, s.split()))
    # ans = []
    # for a in arr:
    #     res = ''
    #     for i in range(len(a)):
    #         if i == 0:
    #             res += a[i].upper()
    #         else:
    #             res += a[i].lower()
    #     ans.append(res)
    # answer = ''
    # for j in range(len(ans)):
    #     if j == 0:
    #         answer += ans[j]
    #     else:
    #         answer += ' ' + ans[j]

s = "3people unFollowed me"
print(solution(s))