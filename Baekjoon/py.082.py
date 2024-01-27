N, K = map(int, input().split())

N_list = []
for n in range(1, N+1):
    if N % n == 0:
        N_list.append(n)
    
s_N_list = sorted(N_list)
if K > len(s_N_list):
    print(0)
else:
    print(s_N_list[K-1])