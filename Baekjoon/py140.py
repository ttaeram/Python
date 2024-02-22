string = input()
bomb = list(map(str, input().strip()))
stack = []

for i in range(len(string)):
    stack.append(string[i])

    if stack[len(stack) - len(bomb) : len(stack)] == bomb:
        for j in range(len(bomb)):
            stack.pop()

if stack:
    print(*stack, sep = '')
else:
    print('FRULA')

# while True:
#     if bomb in string:
#         arr = string.split(bomb)
#         string = ''
#         for n in arr:
#             string += n
#     else:
#         if len(string) > 0:
#             print(string)
#             break
#         else:
#             print('FRULA')
#             break