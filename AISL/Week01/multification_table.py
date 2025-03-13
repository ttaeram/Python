# 초기화
def init():
    print("-" * 55)
    print('"구구단을 외자, 구구단을 외자" 프로그램을 실행합니다.')
    print("1. 홀수 구구단")
    print("2. 짝수 구구단")
    print("3. 종료")
    print("-" * 55)
    print("숫자를 입력하세요:", end = "")

    input_logic()

# 사용자에게 입력값을 받는 기능
def input_logic():
    num = input().strip()

    if num == "1":
        odd()
    
    elif num == "2":
        even()
    
    elif num == "3":
        exit_code()
    
    else:
        error_message()

# 1, 2, 3을 제외한 문자를 입력한 경우
def error_message():
    print("잘못 입력하셨습니다. 1~3 번 숫자를 입력하세요.")
    init()

# 1을 입력한 경우
def odd():
    for n in range(3, 10, 2):
        print(f"{n}단")
        
        for i in range(1, 10):
            print(f"{n} * {i} = {n * i}")
    
    init()

# 2를 입력한 경우
def even():
    n = 2

    while n < 10:
        print(f"{n}단")
        
        for i in range(1, 10):
            print(f"{n} * {i} = {n * i}")
        
        n += 2
    
    init()

# 3을 입력한 경우
def exit_code():
    print("프로그램을 종료합니다.")

init()