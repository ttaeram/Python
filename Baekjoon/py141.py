import sys

def round_(num):
  if num - int(num) >= 0.5:
    return int(num)+1
  else:
    return int(num)

n = int(sys.stdin.readline().strip())
if n:
  level = []
  for _ in range(n):
    level.append(int(sys.stdin.readline().strip()))

  delete = round_(n * 0.15)
  level.sort()
  if delete > 0:
    print(round_(sum(level[delete:-delete])/len(level[delete:-delete])))
  else:
    print(round_(sum(level)/len(level)))
else:
  print(0)