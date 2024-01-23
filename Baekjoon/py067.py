ABC = []
for subject in range(20):
    g = input().split()
    if g[2] == 'P':
        pass
    else:
        ABC.append(g)

def grade_calcilator(g):
    if g == 'A+':
        return 4.5
    elif g == 'A0':
        return 4.0
    elif g == 'B+':
        return 3.5
    elif g == 'B0':
        return 3.0
    elif g == 'C+':
        return 2.5
    elif g == 'C0':
        return 2.0
    elif g == 'D+':
        return 1.5
    elif g == 'D0':
        return 1.0
    else:
        return 0.0

total = 0
totall = 0
for i in range(len(ABC)):
    total = total + ((float(ABC[i][1])) * float(grade_calcilator(ABC[i][2])))

for j in range(len(ABC)):
    totall = totall + (float(ABC[j][1]))
if len(ABC) == 0:
    print(0.0)
else:
    print(total/totall)
# total = 0
# totall = 0
# for A in ABC:
#     if A[2] == 'A+':
#         total += 4.5 * float(A[1])
#         totall += float(A[1])
#     elif A[2] == 'A0':
#         total += 4.0 * float(A[1])
#         totall += float(A[1])
#     elif A[2] == 'B+':
#         total += 3.5 * float(A[1])
#         totall += float(A[1])
#     elif A[2] == 'B0':
#         total += 3.0 * float(A[1])
#         totall += float(A[1])
#     elif A[2] == 'C+':
#         total += 2.5 * float(A[1])
#         totall += float(A[1])
#     elif A[2] == 'C0':
#         total += 2.0 * float(A[1])
#         totall += float(A[1])
#     elif A[2] == 'D+':
#         total += 1.5 * float(A[1])
#         totall += float(A[1])
#     elif A[2] == 'D0':
#         total += 1.0 * float(A[1])
#         totall += float(A[1])
#     elif A[2] == 'F':
#         total += 0
#         totall += 0
# if totall == 0:
#     print(0)
# else:
#     print(total/totall)