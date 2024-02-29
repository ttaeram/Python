N = int(input())
line = list(map(int, input().split()))

line.sort()

ans = 0
stack = 0
for n in range(N):
    stack += line[n]
    ans += stack

print(ans)