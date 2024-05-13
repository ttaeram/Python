import sys
input = sys.stdin.readline

N = int(input())
arr = []
for a in range(N):
    car = input().strip()
    arr.append((a, car))

rra = []
for i in range(N):
    car = input().strip()
    for j in range(N):
        if arr[j][1] == car:
            rra.append((j, car))

ans = 0
for b in range(N):
    idx, car = rra[b]
    for c in range(b, N):
        if rra[c][0] < idx:
            ans += 1
            break

print(ans)