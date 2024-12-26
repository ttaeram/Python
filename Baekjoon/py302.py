import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chik = []
home = []
arr = []

for i in range(N):
    semi = list(map(int, input().split()))
    for j in range(N):
        if semi[j] == 1:
            home.append((i, j))
        elif semi[j] == 2:
            chik.append((i, j))
    arr.append(semi)

def sol():
    

print(arr)
print(chik)
print(home)

각 집에서 치킨집까지의 거리를 싹 추합해놓고 치킨집 줄여가면서 풀면 되는거 아닐까 싶음