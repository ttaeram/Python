import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
n_arr = sorted(list(set(arr)))
dic = {}
for i in range(len(n_arr)):
    dic[n_arr[i]] = i

for j in arr:
    print(dic[j], end = ' ')