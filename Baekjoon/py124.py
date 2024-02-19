N = int(input())

member = []

for n in range(N):
    age, name = map(str, input().split())
    member.append([int(age), name])

member.sort(key = lambda x: x[0])

for m in member:
    print(*m)