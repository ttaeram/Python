from math import *

A, B, V = map(int, input().split())

total = (V-A) / (A - B) + 1
print(ceil(total))