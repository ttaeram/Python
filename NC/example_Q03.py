while True:
    game = input("가위(1), 바위(2), 보(3) 중 선택하세요 (예: 3 2): ")
    A, B = map(int, game.split(' '))

    if A == B:
        print("무승부")
        continue
    elif (A == 1 and B == 3) or (A == 2 and B == 1) or (A == 3 and B == 2):
        print("A")
    else:
        print("B")
    break