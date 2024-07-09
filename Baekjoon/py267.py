from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    semi = list(map(int, input().split()))
    semi = deque(semi)
    arr.append(semi)
print(arr)

for n in range(N):
    one = arr[n][0]
    feild = [0] * 4
