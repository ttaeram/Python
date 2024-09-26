from collections import deque
import sys
input = sys.stdin.readline

N, won = map(str, input().split())
words = [input().strip() for n in range(int(N))]
len_words = {3: [won]}
zzam = []

def mid(now, word):
    now_idx = 0
    word_idx = 0

    while word_idx < len(word):
        if word[word_idx] == now[now_idx]:
            now_idx += 1
        word_idx += 1
    
    if now_idx == len(now):
        return 1
    else:
        return 0

def sol(won):
    global ans
    check = set()
    arr = deque([won])
    check.add(won)

    while arr:
        now = arr.popleft()
        for word in words:
            if word in check or len(word) - 1 != len(now):
                continue
            if word[1:] == now or now == word[:-1] or mid(now, word):
                arr.append(word)
                check.add(word)
                ans = word

ans = won
sol(won)
print(ans)

# for word in zzam:
#     if len(word) > len(ans):
#         ans = word

# ans = won
# leng = len(ans)
# for word in words:
#     idx = 0
#     for w in word:
#         if idx == 3:
#             break

#         if w == won[idx]:
#             idx += 1
#     if idx == 3:
#         if len(word) > leng:
#             ans = word
#             leng = len(word)
#     print(ans)
# print(ans)