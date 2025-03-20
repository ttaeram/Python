import sys

file_path = "/Users/ramy/Desktop/Python/AISL/Week02/tower_of_hanoi/input.txt"
sys.stdin = open(file_path)

# 초기화
def init():
    N = int(input())

    print_ans(N)

    move(N, 1, 3)


# 시행 횟수를 출력
def print_ans(N):
    movement = 2 ** N - 1
    print(movement)


# 하노이 탑 이동
def move(n, start, end):
    if n == 1:
        print(start, end)
        return
    
    move(n - 1, start, 6 - (start + end))
    print(start, end)
    move(n - 1, 6 - (start + end), end)

init()