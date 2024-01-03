n = "6789"
digits = [int(digit) for digit in n]
tot = 0
for s in digits:
    tot += s
print(tot)