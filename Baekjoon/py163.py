N = int(input())
stairs = [0] * 301
for n in range(1, N + 1):
    stairs[n] = int(input())

sol = [0] * 301
sol[1] = stairs[1]
sol[2] = stairs[1] + stairs[2]
sol[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

if N > 3:
    for i in range(4, N + 1):
        sol[i] = max(sol[i - 3] + stairs[i - 1] + stairs[i], sol[i - 2] + stairs[i])

print(sol[N])