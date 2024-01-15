from math import *
t = 3
input_1 = [3, 17, 1, 39, 8, 41, 2, 32, 99, 2]
input_2 = [22, 8, 5, 123, 7, 2, 63, 7, 3, 46]
input_3 = [6, 63, 2, 3, 58, 76, 21, 33, 8, 1]
input = [input_1, input_2, input_3]

for r in range(t):
    odds = 0
    for odd in input[r]:
        if odd % 2 == 1:
            odds += odd
    print("#{0} {1}".format(r+1 ,odds))