import sys

file_path = "/Users/ramy/Desktop/Python/AISL/Week03/lifeboat/input.txt"
sys.stdin = open(file_path)

def init():
    T = int(input())
    
    for t in range(T):
        N, limit, people = input_command()
        people.sort()

        start = 0
        end = N - 1

        boats = solution(start, end, limit, people)

        print(boats)


def input_command():
    print("인원을 입력하세요.")

    N = int(input())

    print("구명보트의 무게 제한을 입력하세요. (40 ~ 240)")

    limit = int(input())

    print(f"{N}명의 몸무게를 입력하세요.")

    people = [int(input()) for _ in range(N)]

    return N, limit, people


def solution(start, end, limit, people):
    boats = 0

    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        
        else:
            end -= 1
        
        boats += 1
    
    return boats


init()