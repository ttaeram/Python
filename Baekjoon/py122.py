while True:
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break
    if A**2 + B**2 == C**2:
        print('right')
    elif C**2 + B**2 == A**2:
        print('right')
    elif A**2 + C**2 == B**2:
        print('right')
    else:
        print('wrong')