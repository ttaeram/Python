import sys
input = sys.stdin.readline

N, K = map(int, input().split())
therm = list(map(int, input().split()))
max_list = []
max_list.append(sum(therm[:K]))

for i in range(N - K):
    max_list.append(max_list[i] - therm[i] + therm[i+K])

print(max(max_list))