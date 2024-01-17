nums = []
for i in range(10):
    A = int(input())
    nums.append(A)

remains = []
for _ in nums:
    remain = _ % 42
    remains.append(remain)

remains = set(remains)
print(len(remains))