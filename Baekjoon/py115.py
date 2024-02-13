N = int(input())
postfix = list(map(str,input().strip()))

alpha = 65
for n in range(N):
    chr(alpha) = input()

for i in range(len(postfix)):
    if postfix[i] not in '*/+-':
        postfix[i] = input()
print(ord('A'))
# stack = []

# for tk in fx:
#     if tk.isnumeric():
#         stack.a1ppend(int(tk))
#     elif tk != ' ':
#         n2 = stack.pop()
#         n1 = stack.pop()
#         if tk == '+':
#             res = n1 + n2
#         elif tk == '-':
#             res = n1 - n2
#         elif tk == '*':
#             res = n1 * n2
#         elif tk == '/':
#             res = n1 // n2
#         stack.append(res)
# print(result)