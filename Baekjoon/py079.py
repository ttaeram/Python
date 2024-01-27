N = int(input())

word_list = []
for i in range(N):
    word_list.append(input())

word_list_sort = sorted(list(set(word_list)))

for i in range(1, 51):
    for word in word_list_sort:
        if len(word) == i:
            print(word)