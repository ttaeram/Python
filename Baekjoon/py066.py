num = int(input())
cnt = 0

for i in range(num):
    words = input() # i-th 단어 입력
    bow = []
    # 만약 문자열이 1개로만 이루어져있다면 그룹단어임.
    if len(words) == 1:
        cnt += 1
    else: 
        for j in range(len(words)):
            if j == 0:
                bow.append(words[0])
            elif j > 0:
                if words[j] == words[j-1]:
                    bow.append(words[j])
                    if j == len(words)-1:
                        cnt += 1
                    
                elif words[j] != words[j-1]: # j번째 철자가 앞의 철자와 다를 때
                    if words[j] not in bow:
                        if j == len(words)-1:
                            cnt += 1
                        else:
                            bow.append(words[j])
                    elif words[j] in bow: # j번째 철자가 앞에서 등장했다면 중단
                        break
                
print(cnt)