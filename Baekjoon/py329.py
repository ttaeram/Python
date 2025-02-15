import sys
input = sys.stdin.readline

def sol():
    for i in range(N):
        for j in range(len(edge)):
            cur, next, cost = edge[j]

            if dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost

                if i == N - 1:
                    return True
    
    return False

T = int(input())

for t in range(T):
    N, M, W = map(int, input().split())
    edge = []
    dist = [int(1e9)] * (N + 1)

    for i in range(M + W):
        S, E, T = map(int, input().split())

        if i >= M:
            T = -T

        else:
            edge.append((E, S, T))

        edge.append((S, E, T))
    
    if sol():
        print("YES")
    
    else:
        print("NO")