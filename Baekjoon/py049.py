T = int(input())

RS_list = []
for _ in range(T):
    RS_list.append(list(map(str, input().split())))

for two_list in RS_list:
    mult = int(two_list[0])
    for rS in two_list[1]:
        print(rS * mult, end = '')
    print()