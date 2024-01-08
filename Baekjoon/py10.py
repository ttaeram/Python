first = input()
second = input()

out_1 = int(first[2])*int(second[2]) + int(first[1])*10*int(second[2]) + int(first[0])*100*int(second[2])
out_2 = int(first[2])*int(second[1]) + int(first[1])*10*int(second[1]) + int(first[0])*100*int(second[1])
out_3 = int(first[2])*int(second[0]) + int(first[1])*10*int(second[0]) + int(first[0])*100*int(second[0])
out_4 = out_1 + out_2 * 10 + out_3 * 100

print(out_1)
print(out_2)
print(out_3)
print(out_4)