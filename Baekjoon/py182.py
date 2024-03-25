N = int(input())
arr = list(map(int, input().split()))
n_arr = sorted(arr)
idx_arr = []
for val in n_arr:
    for i, res in enumerate(arr):
        if res == val:
            idx_arr.append(i)
    
print(idx_arr)