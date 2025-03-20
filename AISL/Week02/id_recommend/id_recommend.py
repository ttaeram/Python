import sys

file_path = "/Users/ramy/Desktop/Python/AISL/Week02/id_recommend/input.txt"
sys.stdin = open(file_path)


# 초기화
def init():
    T = int(input())

    for tc in range(1, T + 1):
        new_id = input().strip()
    
        recommend(new_id)


# 아이디 추천 과정
def recommend(new_id):
    new_id = step1(new_id)
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    new_id = step7(new_id)

    print(new_id)


# 대문자를 소문자로 치환
def step1(new_id):
    result = new_id.lower()

    return result


# 알파벳, 숫자, -, _, . 제외 제거
def step2(new_id):
    can = ["-", "_", "."]
    result = ""

    for s in new_id:
        if s in can:
            result += s
        
        elif s.isalnum():
            result += s
    
    return result


# 중복된 . 제거
def step3(new_id):
    result = ""

    for i in range(len(new_id)):
        if new_id[i] == ".":
            if i > 0 and new_id[i - 1] == ".":
                continue

            else:
                result += new_id[i]
        
        else:
            result += new_id[i]
    
    return result
    

# 문자열 맨 처음, 맨 끝의 . 제거
def step4(new_id):
    result = new_id.strip(".")

    return result


# 빈 문자열에 a 추가
def step5(new_id):
    if new_id == "":
        return "a"
    
    else:
        return new_id


# 16글자 이상일 시 15글자로 만든 후 . 제거
def step6(new_id):
    result = new_id[:15]

    return result.strip(".")


# 2글자 이하의 문자열 3글자로 만들기
def step7(new_id):
    if len(new_id) <= 2:
        s = new_id[-1]

        while len(new_id) != 3:
            new_id += s

    return new_id

init()