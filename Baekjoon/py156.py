import heapq
N = int(input())
deck = []
for n in range(N):
    heapq.heappush(deck, int(input()))

cnt = 0
while len(deck) >= 2:
    a = heapq.heappop(deck)
    b = heapq.heappop(deck)
    cnt += a + b
    heapq.heappush(deck, a + b)

print(cnt)