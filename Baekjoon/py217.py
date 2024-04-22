import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M != 0:
    arr = list(map(int, input().split()))

button = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pos = 100
tar = str(N)
posstr = ''
for n in len(N):
    if N[n] in arr:
        if N[n] < len(N) - 1:

        i = 1
        ch = int(N[n])
        cand = []
        while True:
            if (ch - i) not in arr:
                if (ch + i) in arr:
                    posstr += str(ch - i)
                else:
                    posstr += str(ch + i)