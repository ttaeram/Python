word = input().upper()
word_list = list(set(word))
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) == 1:
    print(word_list[(cnt.index(max(cnt)))])
else:
    print('?')

# word_up = input().upper()

# word_list = []
# for o in word_up:
#     word_list.append(o)

# cnt_list = []
# for w in word_up:
#     cnt = word_up.count(w)
#     cnt_list.append(cnt)

# result_list = []
# max_num = max(cnt_list)
# for num in range(len(cnt_list)):
#     if cnt_list[num] == max_num:
#         result_list.append(word_list[num])

# result_set = set(result_list)
# result_list_real = list(result_set)

# if len(result_list_real) == 1:
#     print(result_list_real[0])
# else:
#     print('?')