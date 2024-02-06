N = int(input())

n = 2
while N > 1:
    if N % n == 0:
        N = N // n
        print(n) 
    elif N % n != 0:
        n += 1