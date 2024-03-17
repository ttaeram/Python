import sys
input = sys.stdin.readline
 
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
inp_1 = input().strip()
inp_2 = input().strip()

arr = []
i = 0
while alpha:
    for r in range(5):
        m_arr = []
        while len(m_arr) < 5:
            for j in range(i, len(inp_2)):
                if inp_2[j] in alpha:
                    m_arr.append(inp_2[j])
                    alpha.remove(inp_2[j])
                if len(m_arr) == 5:
                    break
                if j == len(inp_2):
                    break
            if j == len(inp_2) - 1:
                m_arr.append(alpha[0])
                alpha.pop(0)
            i = j
        arr.append(m_arr)

arr_dict = {}
for r in range(5):
    for c in range(5):
        arr_dict[arr[r][c]] = (r, c)

pw = []
i = 0
while True:
    if i == len(inp_1) - 1:
        pw.append((inp_1[i], 'X'))
        break
    if inp_1[i] != inp_1[i + 1]:
        pw.append((inp_1[i], inp_1[i + 1]))
        i += 2
    else:
        if inp_1[i] == 'X' and inp_1[i + 1] == 'X':
            pw.append((inp_1[i], 'Q'))
        else:
            pw.append((inp_1[i], 'X'))
        i += 1
    if i == len(inp_1):
        break

new_pw = []
for p in pw:
    new_p = []
    a_1 = arr_dict[p[0]]
    a_2 = arr_dict[p[1]]
    if a_1[0] == a_2[0]:
        new_p.append(arr[a_1[0]][((a_1[1] + 1) % 5)])
        new_p.append(arr[a_2[0]][((a_2[1] + 1) % 5)])
        new_pw.append(new_p)
    elif a_1[1] == a_2[1]:
        new_p.append(arr[((a_1[0] + 1) % 5)][a_1[1]])
        new_p.append(arr[((a_2[0] + 1) % 5)][a_2[1]])
        new_pw.append(new_p)
    else:
        new_p.append(arr[a_1[0]][a_2[1]])
        new_p.append(arr[a_2[0]][a_1[1]])
        new_pw.append(new_p)

for aaa in new_pw:
    print(*aaa, sep='', end='')