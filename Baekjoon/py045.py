T = int(input())

word_list = []
for _ in range(T):
    word = str(input())
    word_list.append(word)

for _ in range(T):
    print(word_list[_][0], word_list[_][-1], sep = '')