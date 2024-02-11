N = int(input())
arr = list(int(input()) for _ in range(N))
arr_s = sorted(arr)

First = sum(arr) / N
print(round(First))

Second = arr_s[N // 2]
print(Second)

arr_dict = {}
for i in arr_s:
    if i in arr_dict:
        arr_dict[i] += 1
    else:
        arr_dict[i] = 1

max_freq = max(arr_dict.values())
max_list = []

for i in arr_dict:
    if max_freq == arr_dict[i]:
        max_list.append(i)

if len(max_list) > 1:
    Third = max_list[1]
else:
    Third = max_list[0]
print(Third)

Fourth = max(arr) - min(arr)
print(Fourth)