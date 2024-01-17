N = int(input())
grade = list(map(int, input().split()))

new_grade = []
for _ in range(N):
    g = grade[_]/max(grade) * 100
    new_grade.append(g)

m = sum(new_grade)/N
print(m)