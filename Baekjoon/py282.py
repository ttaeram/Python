from itertools import product
import sys
inpt = sys.stdin.readline

def sol(N):
    arr = []
    calc = ['-', '+', '*10+']
    for n in range(1, N+1):
        arr.append(n)
    
    commands = list(product(range(3), repeat=N-1))
    for command in commands:
        ans = str(arr[N-1])
        res = 0
        cand = ''
        for i in range(N-2, -1, -1):
            c = command[i]
            num = arr[i]

            if c == 0:
                ans = str(num) + ' ' + ans
            elif c == 1:
                ans = str(num) + '+' + ans
            else:
                ans = str(num) + '-' + ans

        for n in range(len(ans)):
            if ans[n].isnumeric():
                cand += ans[n]
            elif ans[n] == ' ':
                continue
            else:
                res += int(cand)
                cand = ans[n]
        res += int(cand)

        if res == 0:
            print(ans)

T = int(input())
for t in range(T):
    N = int(input())
    sol(N)
    print()
