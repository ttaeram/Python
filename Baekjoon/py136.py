N = int(input())
string = input()
r = 31
M = 1234567891
ans = 0

for i in range(N):
    string_num = ord(string[i]) - 96
    ans += string_num * (r ** i)

print(ans % M)