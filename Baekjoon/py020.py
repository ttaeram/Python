A, B, C = map(int, input().split())

list = [A, B, C]
slist = sorted(list, reverse = True)

if A == B == C:
    reward = 10000 + A * 1000
    print(reward)
elif A == B or A == C or B == C:
    reward = 1000 + int(slist[1]) * 100
    print(reward)
else:
    reward = int(slist[0]) * 100
    print(reward)