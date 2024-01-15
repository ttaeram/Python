N, X = map(int, input().split())
A = list(map(int, input().split()))
B = []

for i in A:
    if i < X:
        B.append(str(i))


print(" ".join(B))