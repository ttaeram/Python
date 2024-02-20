gwal = ['(', '{', '[']
ho = [')', '}', ']']


while True:
    string = input()
    if string == '.':
        break
    
    stack = []
    flag = True
    for s in string:
        if not stack:
            if s in gwal:
                stack.append(s)
            elif s in ho:
                flag = False
                break
        elif stack:
            if s in gwal:
                stack.append(s)
            elif s == ho[0]:
                if stack[-1] == gwal[0]:
                    stack.pop()
                elif stack[-1] != gwal[0]:
                    flag = False
                    break
            elif s == ho[1]:
                if stack[-1] == gwal[1]:
                    stack.pop()
                elif stack[-1] != gwal[1]:
                    flag = False
                    break
            elif s == ho[2]:
                if stack[-1] == gwal[2]:
                    stack.pop()
                elif stack[-1] != gwal[2]:
                    flag = False
                    break
    if stack:
        flag = False

    if flag == True:
        print('yes')
    elif flag == False:
        print('no')