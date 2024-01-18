A, B = input().split()

A_sang = int(A[::-1])
B_sang = int(B[::-1])

if A_sang > B_sang:
    print(A_sang)
else:
    print(B_sang)