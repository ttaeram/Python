lst = ['-', '_', '.']
def solution(new_id):
    new_text = ''
    new_id = new_id.lower()
    for i in range(len(new_id)):
        if new_id[i].isalpha() == False:
            if new_id[i].isnumeric() == False:
                if new_id[i] not in lst:
                    continue
                else:
                    new_text += new_id[i]
            else:
                new_text += new_id[i]
        else:
            new_text += new_id[i]

    text_lst = []
    for j in range(len(new_text)):
        if len(text_lst) > 1:
            if text_lst[-1] == '.' and text_lst[-2] == '.':
                text_lst.pop()
        text_lst.append(new_text[j])
    new_text = ''.join(text_lst)

    new_text = new_text.strip('.')

    if len(new_text) == 0:
        new_text = 'a'
    
    if len(new_text) >= 16:
        new_text = new_text[0:15]

    new_text = new_text.strip('.')
    
    if len(new_text) <= 2:
        while len(new_text) < 3:
            new_text += new_text[-1]

    answer = new_text
    return answer
print(solution("123_.def"))