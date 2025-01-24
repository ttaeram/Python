import sys
input = sys.stdin.readline

def sol():
    N, M = map(int, input().split())
    knows = set(input().split()[1:])
    parties = [set(input().split()[1:]) for _ in range(M)]

    for _ in range(M):
        for party in parties:
            if party.intersection(knows):
                knows = knows.union(party)

    cnt = 0

    for party in parties:
        if party & knows:
            continue
        cnt += 1
    
    return cnt

ans = sol()
print(ans)