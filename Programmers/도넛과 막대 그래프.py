def solution(edges):
    N = 0
    for a in edges:
        N = max(N, max(a))
    info = [[] for _ in range(N + 1)]
    check_p = {}
    answer_1 = 0
    answer_2 = 0
    answer_3 = 0
    answer_4 = 0
    for a in edges:
        info[a[0]].append(a[1])
        check_p[a[1]] = 0

    for n in range(1, N + 1):
        if n not in check_p:
            if len(info[answer_1]) < len(info[n]):
                answer_1 = n
        elif len(info[n]) == 0:
            answer_3 += 1
        if len(info[n]) == 2:
            if n in check_p:
                answer_4 += 1
    
    total = len(info[answer_1])
    
    answer_2 = total - (answer_3 + answer_4)
    
    answer = [answer_1, answer_2, answer_3, answer_4]
    print(info)
    return answer

edges = [[2, 3], [2,4]]
print(solution(edges))