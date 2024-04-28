from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        stack = deque()
        stack.append((begin, 0))
        while stack:
            word, cnt = stack.popleft()
            if word == target:
                return cnt
            for wo in words:
                cntt = 0
                for i in range(len(wo)):
                    if wo[i] != word[i]:
                        cntt += 1
                if cntt == 1:
                    stack.append((wo, cnt + 1))

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
ans = solution(begin, target, words)
print(ans)