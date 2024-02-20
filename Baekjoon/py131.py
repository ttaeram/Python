import sys
input = sys.stdin.readline

card_dict = {}
N = int(input())
cards = list(map(int, input().split()))
for card in cards:
    if card not in card_dict:
        card_dict[card] = 1
    elif card in card_dict:
        card_dict[card] += 1

M = int(input())
compare = list(map(int, input().split()))

res = []
for c in compare:
    if c in card_dict:
        res.append(card_dict[c])
    elif c not in card_dict:
        res.append(0)

print(*res)