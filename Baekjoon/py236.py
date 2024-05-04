import sys
input = sys.stdin.readline

K = int(input())
ans = ''
while K > 0:
    if K % 2 == 0:
        ans = '7' + ans
        K -= 2
    else:
        ans = '4' + ans
    K = K // 2
print(ans)


# 1 3 7 15 31

# 4
# 7
# 44
# 47
# 74
# 77
# 444
# 447
# 474
# 477
# 744
# 747
# 774
# 777
# 4444
# 4447
# 4474
# 4477
# 4744
# 4747
# 4774
# 4777
# 7444
# 7447
# 7474
# 7477
# 7744
# 7747
# 7774
# 7777