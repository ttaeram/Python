n = 9
input = "3 17 1 39 8 41 2 32 99"
numbers = list(map(int, input.split(' ')))
numbers.sort()
m = int((n+1)/2)
print(numbers[m])