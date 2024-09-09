import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
if N > 0:
    arr = list(map(int, input().split()))
    arr.sort()
    arr.append(L)

def sol():
    if N > 0:
        ans = L+1
        start = 1
        end = L

        while start <= end:
            mid = (start + end) // 2
            pos = 0
            cnt = 0
            i = 0

            while i < N+1:
                if pos + mid < arr[i]:
                    pos += mid
                    cnt += 1
                else:
                    pos = arr[i]
                    i += 1

            if cnt <= M:
                ans = min(ans, mid)
                end = mid - 1
            else:
                start = mid + 1
    else:
        if L % (M + 1) == 0:
            ans = L // (M + 1)
        else:
            ans = L // (M + 1) + 1
    
    return ans

ans = sol()
print(ans)

