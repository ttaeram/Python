import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = list(map(int, input().split()))

def sol():
    distance = []
    for n in range(N-1):
        distance.append(arr[n+1] - arr[n])
    distance.sort()

    for k in range(K-1):
        distance.pop()
    
    return sum(distance)
    


if N <= K:
    ans = 0

else:
    arr.sort()
    ans = sol()

print(ans)
