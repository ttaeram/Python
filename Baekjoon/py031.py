i = 1
while i >= 0:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A + B)