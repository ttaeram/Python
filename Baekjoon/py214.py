import sys
input = sys.stdin.readline

k = int(input())

def sol(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    if k % 2 == 0:
        return sol(k // 2)
    else:
        return 1 - sol(k // 2)

ans = sol(k - 1)
print(ans)
# def sol(k):
#     if k == 0:
#         return 0
#     elif k == 1:
#         return 1
#     elif k % 2 == 0:
#         sol(k//2)
#     else:
#         return 1 - sol(k//2)
# ans = sol(k - 1)
# print(ans)
# res = '0'

# def sol(res, k):
#     if len(res) >= k:
#         ans = res
#         return ans
#     res_s = ''
#     for i in res:
#         if i == '0':
#             res_s += '1'
#         else:
#             res_s += '0'
#     res += res_s
#     sol(res, k)

# ans = sol(res, k)
# print(ans)