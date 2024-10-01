import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

def sol():
    cnt = 0
    for i in range(N):
        tar = arr[i]
        idx = 0
        end = N-1
        while idx < end:
            if arr[idx] + arr[end] == tar:
                if idx == i:
                    idx += 1
                elif end == i:
                    end -= 1
                else:
                    cnt += 1
                    break

            elif arr[idx] + arr[end] > tar:
                end -= 1

            elif arr[idx] + arr[end] < tar:
                idx += 1
            
    return cnt

ans = sol()
print(ans)