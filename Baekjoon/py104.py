N = int(input())
nums = [int(input()) for _ in range(N)]
reverse_nums = nums[::-1]
s_nums = []

while len(reverse_nums) > 0:
    for n in range(1, nums[0] + 1):
        s_nums.append(n)
        print('+')
    reverse_nums.pop()
    print('-')
    print(nums)