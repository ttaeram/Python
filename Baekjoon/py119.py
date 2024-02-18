dwarf = [int(input()) for _ in range(9)]
dwarf.sort()

height_sum = sum(dwarf)
not_dwarf = []
bp = True

for i in range(9):
    for j in range(i + 1, 9):
        if height_sum - (dwarf[i] + dwarf[j]) == 100:
            not_dwarf.append(dwarf[i])
            not_dwarf.append(dwarf[j])
            bp = False
            break
        else:
            continue
    if bp == False:
        break

for dw in range(9):
    if dwarf[dw] in not_dwarf:
        continue
    else:
        print(dwarf[dw])