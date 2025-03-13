book_info = {
    "HarryPotter1": [[1997], [6], [26]],
    "TheLordOfTheRings": [[1954], [7], [29]],
    "engineering_mathematics1": [[2018], [2], [28]]
}

def init():
    print("원하시는 책을 입력하세요.")
    print(">", end = "")

    input_logic()

def input_logic():
    book = input().strip()

    if book in book_info:
        found_title(book)
    
    else:
        error_message()

def error_message():
    print("제목을 다시 입력해주세요.")
    
    init()

def found_title(book):
    print("-" * 40)
    print("원하시는 정보를 선택해주세요.")
    print("1. 년")
    print("2. 월")
    print("3. 일")
    print("4. 종료")
    print("-" * 40)

    num = int(input())

    if num in (1, 2, 3):
        give_info(book, num)
    
    elif num == 4:
        exit_code()

def give_info(book, n):
    options = ["년", "월", "일"]

    info = book_info[book][n - 1][0]
    option = options[n - 1]

    print(f"{info}{option} 입니다.")

    init()

def exit_code():
    print("프로그램이 종료되었습니다.")

init()