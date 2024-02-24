N = int(input())

cnt = 0
for _ in range(N):
    stack = []
    tar = input()
    for i in range(len(tar)):
        if stack:
            if tar[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(tar[i])
        else:
            stack.append(tar[i])

    if len(stack) == 0:
        cnt += 1
print(cnt)