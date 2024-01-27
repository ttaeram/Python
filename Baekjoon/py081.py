ab_list = []
ab_cnt = 0
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    ab_list.append([a, b])
    ab_cnt += 1

for n in ab_list:
    if float(n[0]/n[1]).is_integer() == True:
        print('multiple')
    elif float(n[1]/n[0]).is_integer() == True:
        print('factor')
    elif float(n[0]/n[1]).is_integer() == False and float(n[1]/n[0]).is_integer() == False:
        print('neither')