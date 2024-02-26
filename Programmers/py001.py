lst = ['-', '_', '.']
def solution(new_id):
    new_text = new_id.lower()
    for i in range(len(new_text)):
        if new_text[i].isalpha() == False:
            if new_text[i] not in lst:
                new_text.replace()
                
    answer = new_text
    return answer
print(solution("...!@BaT#*..y.abcdefghijklm"))