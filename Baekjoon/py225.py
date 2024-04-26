from heapq import heappop, heappush
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    heap_max = []
    heap_min = []
    n = int(input().rstrip())
    visited = [0]*n
    for i in range(n):
        cmd, num = input().rstrip().split()
        num = int(num)
        if cmd == 'I':
            heappush(heap_min, (num, i))
            heappush(heap_max, (-num, i))
            visited[i] = 1 
            # visited의 len을 n으로 설정함으로써
            # 중복되는 num이 들어와도
            # 몇 번째(i번째) 명령에 의한 num인지로 구분 가능
            # num은 가중치로만 사용
        else:
            if num == -1:
                if heap_min:
                    visited[heappop(heap_min)[1]] = 0
            else:
                if heap_max:
                    visited[heappop(heap_max)[1]] = 0
        while heap_min and not visited[heap_min[0][1]]:
            heappop(heap_min)
        while heap_max and not visited[heap_max[0][1]]:
            heappop(heap_max)
    if heap_max:
        print(-heappop(heap_max)[0], heappop(heap_min)[0])
    else:
        print('EMPTY')