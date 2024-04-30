import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    arr = []
    ans = 0
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
        
    arr.sort(key=lambda x: x[0])
    stack = []
    for a, b in arr:
        if not stack:
            ans += 1
            stack.append(b)
        else:
            flag = True
            for i in range(len(stack)):
                if stack[i] <= a:
                    stack[i] = b
                    flag = False
                    break
            if flag:
                ans += 1
                stack.append(b)
    print(ans)
sol()
        # if not stack:
        #     ans += 1
        #     stack.append((a, b))
        # else:
        #     flag = True
        #     for c, d in stack:
        #         if b <= c or d <= a:
        #             flag = False
        #     if flag:
        #         ans += 1
        #         stack.append((a, b))

    # for a, b in rra:
    #     if not kcats:
    #         ans += 1
    #         kcats.append((a, b))
    #     else:
    #         flag = True
    #         for c, d in kcats:
    #             if b <= c or d <= a:
    #                 flag = False
    #         if flag:
    #             ans += 1
    #             kcats.append((a, b))

#     maxL = max(maxL, b)

# hwei = [0] * (maxL + 1)
# for a, b in arr:
#     for i in range(a, b):
#         hwei[i] += 1
# print(max(hwei))