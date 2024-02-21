N = int(input())
NN = str(N)
ans = 0

if len(NN) == 1:
    if N == 3 or N == 5:
        ans += 1
    elif N == 6 or N == 8:
        ans += 2
    elif N == 9:
        ans += 3
elif len(NN) != 1:
    if NN[-1] == '3' or NN[-1] == '8':
        ans += 1 + (N - 3) // 5
    elif NN[-1] == '6' or NN[-1] == '1':
        ans += 2 + (N - 6) // 5
    elif NN[-1] == '9' or NN[-1] == '4':
        ans += 3 + (N - 9) // 5
    elif NN[-1] == '2' or NN[-1] == '7':
        ans += 4 + (N - 12) // 5
    elif NN[-1] == '0' or NN[-1] == '5':
        ans += N // 5

if ans == 0:
    ans -= 1

print(ans)