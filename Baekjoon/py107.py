T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))

    idx = [i for i in range(N)]
    cnt = 0

    while len(importance) > 0:
        if importance[0] == max(importance):
            cnt += 1
            if idx[0] == M:
                print(cnt)
                break
            else:
                importance.pop(0)
                idx.pop(0)
        else:
            importance.append(importance[0])
            importance.pop(0)
            idx.append(idx[0])
            idx.pop(0)