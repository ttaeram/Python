N = int(input())
stack = []
for n in range(N):
    num = int(input())
    if num == 0:
        stack.pop()
    elif num != 0:
        stack.append(num)

if not stack:
    print(0)
else:
    print(sum(stack))