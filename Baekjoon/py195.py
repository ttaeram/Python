import sys
input = sys.stdin.readline

N = int(input())
a, b, c = map(int, input().split())
res_max = [a, b, c]
res_min = [a, b, c]
for n in range(N - 1):
    a, b, c = map(int, input().split())
    res_max = [a + max(res_max[0], res_max[1]), b + max(res_max[0], res_max[1], res_max[2]), c + max(res_max[1], res_max[2])]
    res_min = [a + min(res_min[0], res_min[1]), b + min(res_min[0], res_min[1], res_min[2]), c + min(res_min[1], res_min[2])]
    
print(max(res_max), min(res_min))
