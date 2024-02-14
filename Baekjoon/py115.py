N = int(input())
postfix = list(map(str,input().strip()))

alpha = {}
for n in postfix:
    if n.isupper():
        if n not in alpha:
            alpha[n] = input()
for i in range(len(postfix)):
    if postfix[i] in alpha:
        postfix[i] = alpha[postfix[i]]

stack = []

for tk in postfix:
    if tk not in '*/+-':
        stack.append(int(tk))
    elif tk != ' ':
        n2 = stack.pop()
        n1 = stack.pop()
        if tk == '+':
            res = n1 + n2
        elif tk == '-':
            res = n1 - n2
        elif tk == '*':
            res = n1 * n2
        elif tk == '/':
            res = n1 / n2
        stack.append(res)

result = stack[0]
print('%.2f' %result)