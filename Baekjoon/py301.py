import sys
input = sys.stdin.readline

M1 = " " + input().strip()
M2 = " " + input().strip()

l1, l2 = len(M1) - 1, len(M2) - 1
dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
arr = [[0] * (l2 + 1) for _ in range(l1 + 1)]

def sol():
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if M1[i] == M2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                arr[i][j] = 1
            
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    ans = dp[l1][l2]
    return ans

ans = sol()

print(ans)