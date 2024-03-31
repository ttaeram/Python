import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())

def jae(N, r, c):
    if N == 0:
        return 0
    return (r % 2) * 2 + (c % 2) + 4 * jae(N - 1, int(r / 2), int(c / 2))

ans = jae(N, r, c)
print(ans)