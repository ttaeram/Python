import sys

file_path = "/Users/ramy/Desktop/Python/AISL/Week02/min_sum_and_max_sum/input.txt"
sys.stdin = open(file_path)

import math
import os
import random
import re


# 초기화
def init():
    T = int(input())
    
    for tc in range(1, T + 1):
        print(f"{tc}번 예제")

        if __name__ == '__main__':
            arr = list(map(int, input().rstrip().split()))

            miniMaxSum(arr)


# 최소 합, 최대 합 찾는 기능
def miniMaxSum(arr):
    total = sum(arr)
    min_sum = total
    max_sum = 0
    
    for i in range(5):
        semi = total - arr[i]
        
        min_sum = min_check(min_sum, semi)
        max_sum = max_check(max_sum, semi)
    
    print(min_sum, max_sum)


# 최소 합 판별
def min_check(min_sum, semi):
    if min_sum > semi:
        return semi
    
    else:
        return min_sum


# 최대 합 판별
def max_check(max_sum, semi):
    if max_sum < semi:
        return semi
    
    else:
        return max_sum

init()