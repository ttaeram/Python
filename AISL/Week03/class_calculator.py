class calculator:
    """
    
    """


class improved_calaulator(calculator):
    """
    
    """


def main():
    commands = {
        "1": plus,
        "2": minus
    }

    command = print_script()
    ans = commands.get(command)(1, 3)
    print(ans)


def print_script():
    print("아래에 사용을 원하시는 사칙연산을 선택해주세요!")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 제곱")
    print("6. 최대 공약수")
    print("7. 종료")
    
    command = input().strip()

    return command


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b

main()