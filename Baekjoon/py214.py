import sys
input = sys.stdin.readline

k = int(input())
res = '0'

def sol(res, k):
    if len(res) >= k:
        ans = res
        return ans
    res_s = ''
    for i in res:
        if i == '0':
            res_s += '1'
        else:
            res_s += '0'
    res += res_s
    sol(res, k)

ans = sol(res, k)
print(ans)