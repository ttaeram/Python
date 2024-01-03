from math import *
from random import *
t = 3


for r in range(t):
    max = 0
    input = "3 17 1 39 8 41 2 32 99 2"
    numbers = list(map(int, input.split(' ')))
    for num in numbers:
        if num > max:
            max = num
    print(max)