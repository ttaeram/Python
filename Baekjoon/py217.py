import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M != 0:
    arr = list(map(str, input().split()))

button = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pos = 100
tar = str(N)
T = len(tar)
posstr = ''
for n in range(T-1, -1, -1):
    if tar[n] in arr:
        if n == T - 1:
            ch = int(tar[n])
            i = 1
            while True:
                if str(ch + i) not in arr:
                    if (ch + i) < 10:
                        posstr = str(ch + i)
                        break
                else:
                    if str(ch - i) not in arr:
                        if (ch - i) > -1:
                            posstr = str(ch - i)
                            break
                i += 1
        else:
            cha = int(posstr)
            ch = int(tar[n])
            i = 1
            while True:
                if str(ch + i) not in arr:
                    if (ch + i) < 10:
                        posstr = str(ch + i) + posstr
                        break
                else:
                    if str(ch - i) not in arr:
                        if (ch - i) > -1:
                            posstr = str(ch - i) + posstr
                            break
                i += 1
    else:
        posstr = tar[n] + posstr
print(posstr)
        # if n < len(N) - 1:
        #     pass
        # i = 1
        # ch = int(N[n])
        # cand = []
        # while True:
        #     if (ch - i) not in arr:
        #         if (ch + i) in arr:
        #             posstr += str(ch - i)
        #         else:
        #             posstr += str(ch + i)