fx = input()
postfix = ''
stack = []
priority = {'*': 2, '/': 2, '+': 1, '-': 1}

for tk in fx:
    if tk.isalpha():
        postfix += tk
    elif tk == '(':
        stack.append(tk)
    elif tk == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()
    elif tk in priority:
        while stack and stack[-1] != '(' and (priority[tk] <= priority[stack[-1]]):
            postfix += stack.pop()
        stack.append(tk)

while stack:
    postfix += stack.pop()

print(postfix)