from collections import deque
N, K = map(int, input().split())
M = len(str(N))


def bfs(N, K):
    visited = set()
    visited.add((N, 0))
    q = deque()
    q.append((N, 0))
    answer = 0
    while q:
        n, k = q.popleft()
        if k == K:
            answer = max(answer, n)
            continue
        n = list(str(n))
        for i in range(M-1):
            for j in range(i+1, M):
                if i == 0 and n[j] == '0':
                    continue
                n[i], n[j] = n[j], n[i]
                nn = int(''.join(n))
                if (nn, k+1) not in visited:
                    q.append((nn, k+1))
                    visited.add((nn, k+1))
                n[i], n[j] = n[j], n[i]
    return answer if answer else -1

print(bfs(N, K))

# # 순열 (원본을 교환)
# def perm(time):  # 재귀 도는 횟수 == 숫자를 바꾸는 횟수
#     global max_value, cnt

#     if number[0] == '0':
#         max_value = -1
#         return

#     value = int(''.join(number))

#     if value in checked[time]:  # 중복 방지 가지치기
#         return
#     checked[time].add(value)  # 체크된적이 없으면 등록

#     if time == limit:    # 바꾸는 위치가 N만큼 되면 재귀종료 / N: 리스트의 길이
#         # print(number)
#         # 최대 값인지 확인
#         # print(int(''.join(number)))

#         cnt += 1
#         if max_value < value:
#             max_value = value
#         return

#     else:
#         # 교환 할 index를 위해 for 하나 추가
#         for i in range(N):
#             for j in range(i+1, N):  # 자기 자리를 교환 위치로 보면 안되기 때문에 (숫자 카드 2개를 교환해야 함)
#                 number[i], number[j] = number[j], number[i]
#                 perm(time + 1)
#                 number[i], number[j] = number[j], number[i]

# number, limit = input().split()     # map(int, input().split()) 을 하게되면 number 가 list로 변환하기 복잡해진다.
# number = list(number)
# r_number = ''.join(number)
# limit = int(limit)

# N = len(number)
# max_value = 0
# cnt = 0         # 비교횟수 체크용

# # 횟수별로 가능성 중복 체크
# checked = [set() for _ in range(limit+1)]   # 중복을 방지하기 위한 세트
# perm(0)

# if N == 1:
#     max_value = -1

# print(max_value)
