import sys
input = sys.stdin.readline

N, K = map(int, input().split())

students_0 = [0] * 6
students_1 = [0] * 6
room = 0
for n in range(N):
    a, b = map(int, input().split())
    if a == 0:
        students_0[b - 1] += 1
    elif a == 1:
        students_1[b - 1] += 1

for i in range(6):
    if students_0[i] > K:
        if students_0[i] == 0:
            room += 0
        elif students_0[i] % K == 0:
            room += (students_0[i] // K)
        elif students_0[i] % K != 0:
            room += (students_0[i] // K + 1)
    
    elif students_0[i] <= K:
        if students_0[i] == 0:
            room += 0
        else:
            room += 1

    if students_1[i] > K:
        if students_1[i] % K == 0:
            room += (students_1[i] // K)
        elif students_1[i] % K != 0:
            room += (students_1[i] // K + 1)
    
    elif students_1[i] <= K:
        if students_1[i] == 0:
            room += 0
        else:
            room += 1
    
print(room)