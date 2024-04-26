import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sadari = {}
sadari_start = []
for _ in range(N):
    a, b = map(int, input().split())
    sadari[a] = b
    sadari_start.append(a)
bam = {}
bam_start = []
bam_end = [1]
for _ in range(M):
    a, b = map(int, input().split())
    bam[a] = b
    bam_start.append(a)
    bam_end.append(b)

map = [0] * 101
for idx in bam_start:
    map[idx] = 100
def sol(n):
    for i in range(n, 101):
        if i in bam_start:
            continue
        for j in range(i + 1, i + 7):
            if j <= 100:
                if j in bam_start:
                    if map[bam[j]] != 0:
                        map[bam[j]] = min(map[bam[j]], map[i] + 1)
                    else:
                        map[bam[j]] = map[i] + 1
                if j in sadari_start:
                    if map[j] > 0:
                        map[j] = min((map[i] + 1), map[j])
                        map[sadari[j]] = map[j]
                    else:
                        map[j] = (map[i] + 1)
                        map[sadari[j]] = map[j]
                else:
                    if map[j] > 0:
                        map[j] = min((map[i] + 1), map[j])
                    else:
                        map[j] = map[i] + 1

bam_end.sort()
for n in bam_end:
    sol(n)
print(map)