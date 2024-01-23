N = []

for i in range(5):
    N.append(input())

len_set = set()
for n in N:
    len_set.add(len(n))
max_num = max(len_set)

result = []
for i in range(max_num):
    for n in range(len(N)):
        if max_num > len(N[n]):
            N[n] = N[n]+' '*(max_num-len(N[n]))
        result.append(N[n][i])

while True:
    try:
        result.remove(' ')
    except:
        ' ' not in result
        break

for _ in result:
    print(_, end='')