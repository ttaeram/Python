N = int(input())
students = []

for _ in range(N):
    weight, height = map(int, input().split())
    students.append((weight, height))

for i in students:
    cnt = 1
    for j in students:
        if i[0] < j[0] and i[1] < j[1]:
                cnt += 1
    print(cnt, end = " ")