import sys
input = sys.stdin.readline

def per(n):
    global cnt
    if n == l:
        res = ''.join(arr)
        result.append(res)
        return
    else:
        for i in range(n, l):
            arr[i], arr[n] = arr[n], arr[i]
            per(n + 1)
            arr[i], arr[n] = arr[n], arr[i]

while True:
    data = input().split()
    if len(data) != 2:
        break
    string, N = data
    arr = list(map(str, string.strip()))
    l = len(string)
    N = int(N)
    cnt = 0
    result = []
    per(0)
    result.sort()
    if N > len(result):
        print(string, N, '= No permutation')
        continue
    print(string, N, '=', result[N - 1])