bracket = input()
stack = []
iron = 0
bracket = bracket.replace('()', 'L')

for b in bracket:
    if b == '(':
        stack.append(b)
        iron += 1
    elif b == 'L':
        iron += len(stack)
    elif b == ')':
        stack.pop()

print(iron)