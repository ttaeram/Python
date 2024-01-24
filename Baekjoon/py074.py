N = int(input())

change_list = []
for n in range(N):
    change = int(input())
    change_list.append(change)


for c in change_list:
    cent = []
    cent.append(c // 25)
    c = c % 25
    cent.append(c // 10)
    c = c % 10
    cent.append(c // 5)
    c = c % 5
    cent.append(c // 1)
    for penny in cent:
        print(penny, end = ' ')
    print()