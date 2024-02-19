N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum_cards = cards[i] + cards[j] + cards[k]
            if max_sum < sum_cards <= M:
                max_sum = sum_cards

print(max_sum)
# def subset(cards):
#     result = []
#     def dfs(index, path):
#         if len(path) == 3:
#             result.append(path)

#         for i in range(index, len(cards)):
#             dfs(i + 1, path + [cards[i]])
    
#     dfs(0, [])
#     return result

# subset_cards = subset(cards)
# sum_cards = []

# for c in subset_cards:
#     sum_cards.append(sum(c))

# max_sum = 0
# for i in range(len(sum_cards)):
#     if max_sum < sum_cards[i] <= M:
#         max_sum = sum_cards[i]

# print(max_sum)