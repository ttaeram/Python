import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for n in range(N):
    cand = []
    string = input().strip()
    for m in range(M):
        cand.append(int(string[m]))
    arr.append(cand)

def oneLineN():
    ans = 0
    for i in range(M-2):
        for j in range(i+1, M-1):
            fir = sum(arr[0][:i+1])
            sec = sum(arr[0][i+1:j+1])
            thi = sum(arr[0][j+1:])
            res = fir * sec * thi
            ans = max(ans, res)
    return ans

def oneLineM():
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            fir = sum(arr[:i+1][0])
            sec = sum(arr[i+1:j+1][0])
            thi = sum(arr[j+1:][0])
            res = fir * sec * thi
            ans = max(ans, res)
    return ans

def calc(i, j):
    fir, sec, thi, fou = 0, 0, 0, 0
    ans = 0
    for x in range(N):
        for y in range(M):
            if 0 <= x < i:
                if 0 <= y < j:
                    fir += arr[x][y]
                else:
                    sec += arr[x][y]
            else:
                if 0 <= y < j:
                    thi += arr[x][y]
                else:
                    fou += arr[x][y]
            
    res1 = (fir+sec) * thi * fou
    res2 = fir * (sec+thi) * fou
    res3 = fir * sec * (thi+fou)
    res4 = sec * thi * (fou+fir)

    ans = max(res1, res2, res3, res4)
    return ans

def calcga():
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            fir, sec, thi = 0, 0, 0
            for ar in arr[:i+1]:
                fir += sum(ar)
            for ar in arr[i+1:j+1]:
                sec += sum(ar)
            for ar in arr[j+1:]:
                thi += sum(ar)
            res = fir * sec * thi
            ans = max(ans, res)
    return ans

def calcse():
    ans = 0
    for i in range(M-2):
        for j in range(i+1, M-1):
            fir, sec, thi = 0, 0, 0
            for ar in arr:
                fir += sum(ar[:i+1])
                sec += sum(ar[i+1:j+1])
                thi += sum(ar[j+1:])
            res = fir * sec * thi
            ans = max(ans, res)
    return ans

def other():
    ans = 0
    for i in range(N):
        for j in range(M):
            res1 = calc(i, j)
            ans = max(ans, res1)
    res2 = calcga()
    res3 = calcse()
    print(ans, res2, res3)
    ans = max(ans, res2, res3)
    return ans

if N == 1:
    ans = oneLineN()

elif M == 1:
    ans = oneLineM()

else:
    ans = other()

print(ans)