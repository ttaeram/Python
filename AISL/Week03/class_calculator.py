import math

class calculator:
    def plus(self, a, b):
        return a + b
    

    def minus(self, a, b):
        return a - b
    

    def multiple(self, a, b):
        return a * b
    

    def divide(self, a, b):
        if b == 0:
            return "0으로 나눌 수 없습니다."
        
        else:
            return a / b


class improved_calaulator(calculator):
    def power(self, a, b):
        return a ** b
    

    def gcd(self, a, b):
        return math.gcd(a, b)


def main():
    calc = improved_calaulator()

    commands = {
        "1": calc.plus,
        "2": calc.minus,
        "3": calc.multiple,
        "4": calc.divide,
        "5": calc.power,
        "6": calc.gcd,
        "7": exit_code
    }

    command = print_script()

    if command == "7":
        exit_code()
        return
    
    if command not in commands:
        print("메뉴에 있는 숫자를 입력해주세요.", end = "\n\n")
        return main()
    
    a, b = input_nums()
    ans = commands.get(command)(a, b)
    print(ans, end = "\n\n")
    
    return main()
    

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


def input_nums():
    print("두 숫자를 입력해주세요:", end = " ")

    a, b = map(int, input().split())

    return a, b


def exit_code():
    print("계산기 프로그램을 종료합니다.")


main()