def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)

    ans = 0
    a = 0
    b = 0
    while a < len(A):
        if A[a] < B[b]:
            ans += 1
            b += 1
        a += 1
    return ans

A = [5, 1, 3, 7]
B = [2, 2, 6, 8]
print(solution(A, B))