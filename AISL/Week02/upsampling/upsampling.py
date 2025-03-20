import sys

file_path = "/Users/ramy/Desktop/Python/AISL/Week02/upsampling/input.txt"
sys.stdin = open(file_path)


# 초기화
def init():
    T = int(input())

    for tc in range(1, T + 1):
        N, K = map(int, input().split())
        arr = [list(map(str, input().split())) for _ in range(N)]
        
        answer = upsample(arr, K)
        print_ans(tc, answer)


# 답을 출력하는 기능
def print_ans(tc, answer):
    print(f"{tc}번 예제")
    for row in answer:
        print(" ".join(map(str, row)))


# 업샘플링 기능
def upsample(arr, K):
    if K == 1:
        return arr

    # 행을 K배 복제
    row_expanded = []
    for r in arr:
        for _ in range(K):
            row_expanded.append(r)

    # 열을 K배 복제
    upsampled_arr = []
    
    for row in row_expanded:
        new_row = []

        for val in row:
            new_row.extend([val] * K)

        upsampled_arr.append(new_row)

    return upsampled_arr


init()