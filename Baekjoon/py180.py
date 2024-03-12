import sys
input = sys.stdin.readline

command = input()
stack = []
stack_2 = []
star = ''
for c in command:
    if c == '+' or c == '-':
        stack.append(int(star))
        star = ''
        if c == '-':
            stack_2.append(sum(stack))
            stack = []
    else:
        star += c
if star:
    stack.append(int(star))
    stack_2.append(sum(stack))

ans = stack_2[0]
for n in range(1, len(stack_2)):
    ans -= stack_2[n]

print(ans)