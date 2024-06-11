import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())
a = 0
for i in arr:
    if i % T == 0:
        a += i // T
    else:
        a += ((i // T)+ 1)
b = N // P
c = N % P
print(a)
print(b, c)