import sys
input = sys.stdin.readline

K = int(input())
if K % 2 == 0:
    ans = ((K // 2) - 1) * 10 + 7
else:
    ans = (K // 2) * 10 + 4
print(ans)