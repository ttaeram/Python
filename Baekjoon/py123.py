T = int(input())
for t in range(T):
    stack = []
    flag = True
    gwal = input()

    for g in gwal:
        if len(stack) == 0:
            if g == '(':
                stack.append(g)
            elif g == ')':
                flag = False
                break
        
        else:
            if g == '(':
                stack.append(g)
            elif g == ')':
                stack.pop()
    
    if len(stack) == 0 and flag == True:
        print('YES')
    elif len(stack) > 0 or flag == False:
        print('NO')