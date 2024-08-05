import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

def search(start, end):
    global ans
    while start <= end:
        mid = (start + end) // 2
        current = arr[0]
        count = 1

        for n in range(1, N):
            if arr[n] >= current + mid:
                count += 1
                current = arr[n]

        if count >= C:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

start = 1
end = arr[-1] - arr[0]
ans = 0
search(start, end)

print(ans)