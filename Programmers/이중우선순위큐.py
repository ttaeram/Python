def solution(operations):
    que = []
    for op in operations:
        if 'I' in op:
            que.append(int(op[2:]))
        if que:
            if op == 'D 1':
                que.sort()
                que.pop()
            elif op == 'D -1':
                que.sort()
                que.pop(0)
        else:
            continue
    if que:
        answer = [max(que), min(que)]
    else:
        answer = [0, 0]
    return answer

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))