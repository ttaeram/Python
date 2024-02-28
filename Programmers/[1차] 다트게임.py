def solution(dartResult):
    answer = 0
    stack = []
    flag = True
    
    for i in range(len(dartResult)):
        stack.append(dartResult[i])
        if flag == False:
            a2 = stack.pop()
            a1 = stack.pop()
            stack.append(a1 + a2)
            flag = True
        if dartResult[i].isnumeric() == True:
            if dartResult[i + 1].isnumeric() == True:
                flag = False
                continue
        if dartResult[i].isnumeric():
            stack.append(int(stack.pop()))
        if dartResult[i].isalpha():
            stack.pop()
            if dartResult[i] == 'S':
                continue
            elif dartResult[i] == 'D':
                stack.append(int(stack.pop()) ** 2)
            elif dartResult[i] == 'T':
                stack.append(int(stack.pop()) ** 3)
        elif dartResult[i].isnumeric() == False and dartResult[i].isalpha() == False:
            stack.pop()
            if dartResult[i] == '#':
                stack.append(stack.pop() * -1)
            if dartResult[i] == '*':
                if len(stack) == 1:
                    stack.append(stack.pop() * 2)
                if len(stack) > 1:
                    n2 = stack.pop()
                    n1 = stack.pop()
                    stack.append(n1 * 2)
                    stack.append(n2 * 2)
    answer = sum(stack)

    return answer

dartResult = input()
print(solution(dartResult))