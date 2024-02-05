N = int(input())
A_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

def binarysearch(a, N, key):
    start = 0
    end = N -1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return 1
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return 0

A_sorted = sorted(A_list)
# min_A = min(A_list)
# max_A = max(A_list)

for i in M_list:
    ans = binarysearch(A_sorted, N, i)
    print(ans)
    # # if min_A <= i <= max_A:
    # if i in A_sorted:
    #     print(1)
    # else:
    #     print(0)