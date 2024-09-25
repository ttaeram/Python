import sys
input = sys.stdin.readline

N = int(input())
opened = list(map(int, input().split()))
U = int(input())

ans = 0
for _ in range(U):
    now = int(input())
    if abs(opened[0] - now) > abs(opened[1] - now):
        ans += abs(opened[1] - now)
        opened[1] = now
    
    else:
        ans += abs(opened[0] - now)
        opened[0] = now
    
print(ans)
