import sys
input = sys.stdin.readline

def sol():
    N, P, Q = map(int, input().split())
    arr = {}
    arr[0] = 1
    ans = 0
    def infin(n):
        if n in arr.keys():
            return arr[n]
        else:
            p = infin(n // P)
            q = infin(n // Q)
            arr[n] = p + q
            return arr[n]
    ans = infin(N)
    print(ans)

sol()