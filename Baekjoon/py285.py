from collections import deque
import sys
input = sys.stdin.readline

V = int(input())
arr = [[] for _ in range(V + 1)]

def tree(pos):
    check = [-1] * (V + 1)
    check[pos] = 0

    res = deque()
    res.append(pos)

    while res:
        pos = res.popleft()
        for command in arr[pos]:
            n, d = command

            if check[n] == -1:
                res.append(n)
                check[n] = check[pos] + d
    
    ans = max(check)
    idx = check.index(ans)

    return (ans, idx)

def sol():
    for v in range(V):
        info = list(map(int, input().split()))
        for i in range(1, len(info) -2, 2):
            arr[info[0]].append((info[i], info[i+1]))
    
    res = tree(1)[1]
    ans = tree(res)[0]
    return ans

ans = sol()
print(ans)