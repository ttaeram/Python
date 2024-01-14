total = int(input())
cnt = int(input())
cal = 0
for N in range(1, cnt+1):
    a, b = map(int, input().split())
    cal += a*b
if cal == total:
    print("Yes")
else:
    print("No")