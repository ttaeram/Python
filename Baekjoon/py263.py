import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
ans_1 = A + B - C

A, B = str(A), str(B)
ans_2 = A + B
ans_2 = int(ans_2) - C

print(ans_1)
print(ans_2)