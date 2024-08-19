N = int(input())
arr = list(map(int, input().split()))

def sol():
    i, j = 0, 1
    kind = [arr[0]]
    ans = 0
    next = 0
    while j < N:
        if len(kind) == 1:
            if arr[j] not in kind:
                kind.append(arr[j])

        else:
            if arr[j] not in kind:
                ans = max(ans, j - i)

                for n in range(len(kind)):
                    if kind[n] != arr[next]:
                        kind.pop(n)
                        break

                kind.append(arr[j])
                i = next

        if arr[j - 1] != arr[j]:
            next = j
        j += 1

    ans = max(ans, N-i)
    return ans
ans = sol()
print(ans)