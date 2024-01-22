word = input()

word_list = []
for w in word:
    word_list.append(w)

reverse_list = word_list[::-1]
reverse_word = ''.join(reverse_list)

if reverse_word == word:
    print(1)
else:
    print(0)