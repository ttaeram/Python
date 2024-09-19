import sys
input = sys.stdin.readline

N = int(input())

def check(res):
    leng = len(res)
    for i in range(1, leng//2 + 1):
        if res[-i:] == res[-(i*2):-i]:
            return False
    else:
        return True

def sol(res):
    if len(res) == N:
        print(res)
        exit()
    
    for i in '123':
        if check(res + i):
            sol(res + i)
    
    return

sol('1')